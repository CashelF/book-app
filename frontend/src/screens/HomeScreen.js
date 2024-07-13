import React, { useEffect, useState } from 'react';
import { View, Text, Image, ScrollView, TouchableOpacity, StyleSheet, ActivityIndicator } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import SearchBar from "react-native-dynamic-search-bar";
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';

const HomeScreen = () => {
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
    <View style={styles.outerContainer}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.header}>
          <Ionicons name="menu" size={32} color="black" style={styles.menuIcon} />
          <View style={styles.circleIcon}></View>
        </View>
        <View style={styles.headerTextContainer}>
          <Text style={styles.welcomeText}>Welcome back, Bunny!</Text>
          <Text style={styles.subHeaderText}>Here are your saved and suggested books!</Text>
        </View>
        <SearchBar
          style={styles.searchBar}
          placeholder="Search here"
          onPress={() => alert("onPress")}
          onChangeText={(text) => console.log(text)}
        />
        <View style={styles.buttonLayout}>
          <TouchableOpacity style={styles.button}>
            <Text style={styles.buttonText}>Saved</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button}>
            <Text style={styles.buttonText}>Suggested</Text>
          </TouchableOpacity>
        </View>
        <View style={styles.bookList}>
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
        </View>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  outerContainer: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  scrollContainer: {
    flexGrow: 1,
    paddingHorizontal: 20,
    paddingBottom: 20,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 20,
  },
  headerTextContainer: {
    marginBottom: 20,
  },
  welcomeText: {
    color: "#9D9D9D",
    fontSize: 16,
  },
  subHeaderText: {
    color: "#19191B",
    fontSize: 26,
  },
  searchBar: {
    width: "100%",
    marginTop: 20,
    backgroundColor: 'rgba(196, 196, 196, 0.15)',
  },
  buttonLayout: {
    flexDirection: 'row',
    marginTop: 10,
  },
  button: {
    flex: 1,
    height: 50,
    backgroundColor: "white",
    alignItems: 'center',
    justifyContent: 'center',
  },
  buttonText: {
    fontSize: 16,
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
    width: 128,
    height: 200,
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
});

export default HomeScreen;
