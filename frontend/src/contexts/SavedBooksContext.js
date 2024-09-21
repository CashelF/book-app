import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';

export const SavedBooksContext = createContext();

export const SavedBooksProvider = ({ children }) => {
  const [savedBooks, setSavedBooks] = useState([]);

  const fetchSavedBooks = async () => {
    try {
      const token = await AsyncStorage.getItem('access_token');
      const response = await axios.get(`${API_URL}/api/users/savedBooks`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setSavedBooks(response.data);
    } catch (error) {
      console.error('Error fetching saved books:', error);
    }
  };

  // Fetch saved books once when the app starts
  useEffect(() => {
    fetchSavedBooks();
  }, []);

  return (
    <SavedBooksContext.Provider value={{ savedBooks, setSavedBooks, fetchSavedBooks }}>
      {children}
    </SavedBooksContext.Provider>
  );
};
