import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, FlatList, TouchableOpacity, StyleSheet, Alert, Image, Dimensions } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import { Ionicons } from '@expo/vector-icons';
import { API_URL } from '@env';

const ReadingHistoryScreen = ({ navigation }) => {
  const [query, setQuery] = useState('');
  const [books, setBooks] = useState([]);
  const [selectedBooks, setSelectedBooks] = useState([]);

  useEffect(() => {
    if (query.length === 0) {
      fetchContentBasedRecommendations();
    }
  }, [query]);

  const fetchContentBasedRecommendations = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const response = await axios.get(`${API_URL}/api/recommendations/content-based`, {
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json',
        },
      });
      setBooks(response.data);
    } catch (error) {
      console.error('Error fetching content-based recommendations:', error);
    }
  };

  const searchBooks = async (text) => {
    setQuery(text);
    if (text.length > 1) {
      try {
        const token = await AsyncStorage.getItem('access_token');
        const response = await axios.get(`${API_URL}/api/books/search`, {
          params: { q: text },
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });
        setBooks(response.data);
      } catch (error) {
        console.error('Error searching books:', error);
      }
    } else {
      fetchContentBasedRecommendations();
    }
  };

  const selectBook = async (book) => {
    const updatedSelectedBooks = selectedBooks.includes(book)
      ? selectedBooks.filter((b) => b !== book)
      : [...selectedBooks, book];

    setSelectedBooks(updatedSelectedBooks);

    try {
      const token = await AsyncStorage.getItem('access_token');
      await axios.post(
        `${API_URL}/api/users/readingHistory`,
        { books: updatedSelectedBooks },
        {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        }
      );
      await axios.post(
        `${API_URL}/api/users/preference-embedding`,
        { books: updatedSelectedBooks },
        {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        }
      );
    } catch (error) {
      console.error('Error updating reading history and preference embedding:', error);
      Alert.alert('Error updating reading history. Please try again.');
    }
  };

  const handleSubmit = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const response = await axios.post(
        `${API_URL}/api/users/readingHistory`,
        { books: selectedBooks },
        {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        }
      );
      if (response.status === 201) {
        navigation.navigate('Home');
      }
    } catch (error) {
      console.error('Error submitting books:', error);
      Alert.alert('Error submitting books. Please try again.');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Search and select books you've read</Text>
      <TextInput
        style={styles.input}
        placeholder="Search for books"
        value={query}
        onChangeText={searchBooks}
      />
      <FlatList
        contentContainerStyle={styles.bookList}
        data={books}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity style={styles.bookItem} onPress={() => selectBook(item)}>
            <Image style={styles.bookImage} source={{ uri: item.cover_image_url }} />
            {selectedBooks.includes(item) && (
              <View style={styles.checkmarkContainer}>
                <Ionicons name="checkmark-circle" size={24} color="green" />
              </View>
            )}
            <Text style={styles.bookTitle} numberOfLines={1}>{item.title}</Text>
            <Text style={styles.bookAuthor} numberOfLines={1}>{item.author}</Text>
          </TouchableOpacity>
        )}
        numColumns={2}
        showsVerticalScrollIndicator={false}
        style={styles.fixedHeightList}
      />
      <TouchableOpacity style={styles.button} onPress={handleSubmit}>
        <Text style={styles.buttonText}>Submit</Text>
      </TouchableOpacity>
    </View>
  );
};

const screenWidth = Dimensions.get('window').width;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
    alignItems: 'center',
    paddingTop: 20,
    paddingLeft: 20,
    paddingRight: 20,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    width: screenWidth > 600 ? '50%' : '90%',
    padding: 10,
    marginVertical: 10,
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 5,
    alignSelf: 'center',
  },
  bookList: {
    paddingBottom: 80,
  },
  bookItem: {
    flex: 1,
    marginHorizontal: 35,
    marginVertical: 10,
    position: 'relative',
    alignItems: 'center',
    justifyContent: 'center',
  },
  bookImage: {
    width: 128,
    height: 200,
    borderRadius: 10,
    marginBottom: 10,
  },
  checkmarkContainer: {
    position: 'absolute',
    top: 10,
    right: 10,
  },
  bookTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    width: 128,
  },
  bookAuthor: {
    fontSize: 14,
    color: '#888',
    textAlign: 'center',
  },
  button: {
    padding: 15,
    backgroundColor: '#FF6B6B',
    borderRadius: 5,
    width: screenWidth > 600 ? '50%' : '90%',
    alignItems: 'center',
    alignSelf: 'center',
    position: 'absolute',
    bottom: 20,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
  },
  fixedHeightList: {
    height: 400, // Set the desired fixed height here
  },
});

export default ReadingHistoryScreen;
