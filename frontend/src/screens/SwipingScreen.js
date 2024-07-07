import React, { useEffect, useState } from 'react';
import { View, Text, Image, StyleSheet, Dimensions, ActivityIndicator, TouchableOpacity } from 'react-native';
import GestureRecognizer from 'react-native-swipe-gestures';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';
import { Ionicons } from '@expo/vector-icons';
import Entypo from '@expo/vector-icons/Entypo';

const { width } = Dimensions.get('window');

const SwipingScreen = () => {
  const [books, setBooks] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    setLoading(true);
    try {
      const token = await AsyncStorage.getItem('access_token');
      const response = await axios.get(`${API_URL}/api/books/`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setBooks(response.data.book);
      setLoading(false);
    } catch (error) {
      console.error(error);
      setLoading(false);
    }
  };

  const onSwipeLeft = () => {
    if (currentIndex < books.length - 1) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const onSwipeRight = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const handleLike = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const currentBook = books[currentIndex];
      await axios.post(
        `${API_URL}/api/interactions/record`,
        {
          book_id: currentBook.id,
          interaction_type: 'like',
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          }
        }
      );
      console.log('Liked:', currentBook.title);
      onSwipeLeft();
    } catch (error) {
      console.error('Error recording like interaction:', error);
    }
  };

  const handleSave = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const currentBook = books[currentIndex];
      await axios.post(
        `${API_URL}/api/interactions/record`,
        {
          book_id: currentBook.id,
          interaction_type: 'save',
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          }
        }
      );
      console.log('Saved:', currentBook.title);
      onSwipeLeft();
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
      onSwipeLeft={onSwipeLeft}
      onSwipeRight={onSwipeRight}
      style={styles.container}
    >
      <View style={styles.card}>
        {currentBook.cover_image ? (
          <Image source={{ uri: currentBook.cover_image }} style={styles.image} />
        ) : (
          <View style={styles.noImage}>
            <Text>No Image Available</Text>
          </View>
        )}
        <Text style={styles.title}>{currentBook.title}</Text>
        <Text style={styles.description}>{currentBook.description}</Text>
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
  card: {
    width: width * 0.8,
    padding: 20,
    borderRadius: 10,
    backgroundColor: '#f9f9f9',
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowRadius: 10,
    alignItems: 'center',
  },
  image: {
    width: 150,
    height: 200,
    resizeMode: 'contain',
    marginBottom: 20,
  },
  noImage: {
    width: 150,
    height: 200,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#ddd',
    marginBottom: 20,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 10,
  },
  description: {
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
