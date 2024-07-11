import React, { useEffect, useState } from 'react';
import { View, Text, Image, ScrollView, TextInput, StyleSheet, ActivityIndicator } from 'react-native';
import { Ionicons, MaterialIcons } from '@expo/vector-icons';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';

const SavedBooksScreen = () => {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSavedBooks();
  }, []);

  const fetchSavedBooks = async () => {
    setLoading(true);
    try {
      const token = await AsyncStorage.getItem('access_token');
      const response = await axios.get(`${API_URL}/api/users/savedBooks`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      console.log('API Response:', response.data); // Log the response data
      if (response.data && response.data.savedBooks) {
        setBooks(response.data.savedBooks);
      } else {
        console.error('Books data not found in response:', response.data);
      }
      setLoading(false);
    } catch (error) {
      console.error('Error fetching saved books:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Ionicons name="menu" size={30} color="black" />
        <Text style={styles.welcome}>Welcome back, Bunny!</Text>
        <Image
          style={styles.profileImage}
          source={require('../../assets/favicon.png')}
        />
      </View>
      <Text style={styles.title}>Here are your saved and suggested books!</Text>
      <View style={styles.searchBar}>
        <Ionicons name="search" size={20} color="black" />
        <TextInput style={styles.searchInput} placeholder="Search" />
      </View>
      <View style={styles.tabs}>
        <Text style={styles.tabActive}>Saved</Text>
        <Text style={styles.tabInactive}>Suggestions</Text>
      </View>
      <ScrollView style={styles.bookList}>
        <View style={styles.bookRow}>
          {books.map((book, index) => (
            <View key={index} style={styles.bookItem}>
              {book.cover_image_url ? (
                <Image style={styles.bookImage} source={{ uri: book.cover_image_url }} />
              ) : (
                <View style={styles.noImage}>
                  <Text>No Image Available</Text>
                </View>
              )}
              <Text style={styles.bookTitle} numberOfLines={1}>{book.title}</Text>
              <Text style={styles.bookAuthor} numberOfLines={1}>{book.authors.map(author => author.name).join(', ')}</Text>
            </View>
          ))}
        </View>
      </ScrollView>
      <View style={styles.footer}>
        <Ionicons name="home" size={30} color="black" />
        <MaterialIcons name="book" size={30} color="black" />
        <Ionicons name="bookmark" size={30} color="black" />
        <Ionicons name="settings" size={30} color="black" />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
    padding: 20,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 20,
  },
  welcome: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  profileImage: {
    width: 40,
    height: 40,
    borderRadius: 20,
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  searchBar: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFF',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 10,
    marginBottom: 20,
  },
  searchInput: {
    flex: 1,
    marginLeft: 10,
  },
  tabs: {
    flexDirection: 'row',
    marginBottom: 20,
  },
  tabActive: {
    fontSize: 16,
    fontWeight: 'bold',
    marginRight: 20,
    borderBottomWidth: 2,
    borderBottomColor: 'red',
  },
  tabInactive: {
    fontSize: 16,
    color: '#888',
  },
  bookList: {
    flex: 1,
  },
  bookRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  bookItem: {
    width: '48%',
    marginBottom: 20,
  },
  bookImage: {
    width: 128,
    height: 200,
    resizeMode: 'cover',
    backgroundColor: '#D45555',
    borderRadius: 20,
    marginBottom: 20,
  },
  noImage: {
    width: '100%',
    height: 150,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#ddd',
    borderRadius: 10,
    marginBottom: 10,
  },
  bookTitle: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  bookAuthor: {
    fontSize: 14,
    color: '#888',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  footer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    paddingVertical: 10,
    borderTopWidth: 1,
    borderTopColor: '#DDD',
  },
});

export default SavedBooksScreen;
