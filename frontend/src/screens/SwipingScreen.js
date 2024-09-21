import React, { useEffect, useState } from 'react';
import { View, Text, Image, StyleSheet, Dimensions, ActivityIndicator, TouchableOpacity, ScrollView } from 'react-native';
import GestureRecognizer from 'react-native-swipe-gestures';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';
import { SavedBooksContext } from '../contexts/SavedBooksContext';
import { Ionicons } from '@expo/vector-icons';
import Entypo from '@expo/vector-icons/Entypo';

const { width } = Dimensions.get('window');

const SwipingScreen = () => {
  const [books, setBooks] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const { savedBooks, setSavedBooks } = React.useContext(SavedBooksContext);

  useEffect(() => {
    fetchBooks();
    postPreferenceEmbedding();
  }, []);

  const fetchBooks = async () => {
    setLoading(true);
    try {
      const token = await AsyncStorage.getItem('access_token');
      const response = await axios.get(`${API_URL}/api/recommendations/content-based`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setBooks(response.data);
      setLoading(false);
    } catch (error) {
      console.error(error);
      setLoading(false);
    }
  };

  const postPreferenceEmbedding = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      await axios.post(
        `${API_URL}/api/users/preference-embedding`,
        {},
        {
          headers: {
            Authorization: `Bearer ${token}`,
          }
        }
      );
      console.log('Preference embedding posted successfully.');
    } catch (error) {
      console.error('Error posting preference embedding:', error);
    }
  };

  const onSwipeUp = () => {
    if (currentIndex < books.length - 1) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const onSwipeDown = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const handleLike = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const currentBook = books[currentIndex];
      await axios.post(
        `${API_URL}/api/interactions/like`,
        {
          book_id: currentBook.id,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          }
        }
      );
    } catch (error) {
      console.error('Error recording like interaction:', error);
    }
  };

  const handleSave = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const currentBook = books[currentIndex];
  
      const isAlreadySaved = savedBooks.some(book => book.id === currentBook.id);
  
      if (isAlreadySaved) {
        await axios.post(
          `${API_URL}/api/interactions/unsave`,
          { book_id: currentBook.id },
          { headers: { Authorization: `Bearer ${token}` } }
        );
  
        setSavedBooks(savedBooks.filter(book => book.id !== currentBook.id));
        return;
      }
  
      await axios.post(
        `${API_URL}/api/interactions/save`,
        { book_id: currentBook.id },
        { headers: { Authorization: `Bearer ${token}` } }
      );
  
      setSavedBooks([...savedBooks, currentBook]);
  
    } catch (error) {
      console.error('Error recording save interaction:', error);
    }
  };
  

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  const currentBook = books[currentIndex];

  return (
    <GestureRecognizer
      onSwipeUp={onSwipeUp}
      onSwipeDown={onSwipeDown}
      style={styles.container}
    >
      <View style={styles.card}>
        {currentBook.cover_image_url ? (
          <Image source={{ uri: currentBook.cover_image_url }} style={styles.image} />
        ) : (
          <View style={styles.noImage}>
            <Text>No Image Available</Text>
          </View>
        )}
        <Text style={styles.title}>{currentBook.title}</Text>
        <Text style={styles.subHeaderText}>Description</Text>
        <View style={styles.descriptionContainer}>
          <ScrollView>
            <Text style={styles.description}>{currentBook.description}</Text>
          </ScrollView>
        </View>
      </View>
      <View style={styles.buttonContainer}>
        <TouchableOpacity onPress={handleSave} style={styles.button}>
          <Entypo name="bookmark" size={72} color="#E94057" style={styles.swipeIcons}/>
        </TouchableOpacity>
        <TouchableOpacity onPress={handleLike} style={styles.button}>
          <Ionicons name="heart-circle" size={72} color="green" />
        </TouchableOpacity>
      </View>
    </GestureRecognizer>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  menuContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  card: {
    padding: 20,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center'
  },
  image: {
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
    borderRadius: 20,
    marginBottom: 20,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 10,
  },
  subHeaderText: {
    marginTop: 10,
    color: '#19191B',
    fontSize: 16,
    fontWeight: 'bold'
  },
  descriptionContainer: {
    height: 350,
    width: '100%',
    marginVertical: 10,
  },
  description: {
    color: '#9D9D9D',
    fontSize: 14,
    textAlign: 'center',
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    width: width * 0.8,
    marginTop: 20,
  },
  button: {
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default SwipingScreen;
