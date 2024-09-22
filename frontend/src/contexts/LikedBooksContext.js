import React, { createContext, useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import { API_URL } from '@env';

export const LikedBooksContext = createContext();

export const LikedBooksProvider = ({ children }) => {
  const [likedBooks, setLikedBooks] = useState([]);

  const fetchLikedBooks = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const response = await axios.get(`${API_URL}/api/users/likedBooks`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setLikedBooks(response.data.likedBooks || []);
    } catch (error) {
      console.error('Error fetching liked books:', error);
    }
  };

  const saveLikedBooksToStorage = async (books) => {
    try {
      await AsyncStorage.setItem('likedBooks', JSON.stringify(books));
    } catch (error) {
      console.error('Error saving liked books to storage:', error);
    }
  };

  return (
    <LikedBooksContext.Provider value={{ likedBooks, setLikedBooks, fetchLikedBooks }}>
      {children}
    </LikedBooksContext.Provider>
  );
};
