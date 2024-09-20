import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Alert, Dimensions } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import { SafeAreaView } from 'react-native-safe-area-context';
import BookList from '../components/BookList'; // Import BookList component
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
    const token = await AsyncStorage.getItem('access_token');
    let updatedSelectedBooks;

    if (selectedBooks.includes(book.id)) {
      // Remove book from reading history
      updatedSelectedBooks = selectedBooks.filter((id) => id !== book.id);
      setSelectedBooks(updatedSelectedBooks);

      try {
        await axios.delete(
          `${API_URL}/api/users/readingHistory`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json',
            },
            data: { book_id: book.id },
          }
        );
        await axios.post(
          `${API_URL}/api/users/preference-embedding`,
          { book_ids: updatedSelectedBooks },
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json',
            },
          }
        );
      } catch (error) {
        console.error('Error removing book:', error);
        Alert.alert('Error updating reading history. Please try again.');
      }
    } else {
      // Add book to reading history
      updatedSelectedBooks = [...selectedBooks, book.id];
      setSelectedBooks(updatedSelectedBooks);

      try {
        await axios.post(
          `${API_URL}/api/users/readingHistory`,
          { book_ids: [book.id] },
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json',
            },
          }
        );
        await axios.post(
          `${API_URL}/api/users/preference-embedding`,
          { book_ids: updatedSelectedBooks },
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json',
            },
          }
        );
      } catch (error) {
        console.error('Error adding book:', error);
        Alert.alert('Error updating reading history. Please try again.');
      }
    }
  };

  const handleSubmit = () => {
    navigation.navigate('Home');
  };

  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Search and select books you've read</Text>
      <TextInput
        style={styles.input}
        placeholder="Search for books"
        value={query}
        onChangeText={searchBooks}
      />
      {/* Use BookList component here */}
      <BookList 
        books={books} 
        onBookPress={selectBook} 
        selectedBooks={selectedBooks}  // Highlight selected books
      />
      <TouchableOpacity style={styles.button} onPress={handleSubmit}>
        <Text style={styles.buttonText}>Submit</Text>
      </TouchableOpacity>
    </SafeAreaView>
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
});

export default ReadingHistoryScreen;
