import React, { useContext, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';
import { View, Text, ScrollView, StyleSheet, ActivityIndicator, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import SearchBar from "react-native-dynamic-search-bar";
import { SavedBooksContext } from '../contexts/SavedBooksContext';
import { UserContext } from '../contexts/UserContext';
import BookList from '../components/BookList';

const SavedBooksScreen = () => {
  const { savedBooks, loading } = useContext(SavedBooksContext);
  const { username, setUsername } = useContext(UserContext);

  useEffect(() => {
    const fetchUserProfile = async () => {
      const token = await AsyncStorage.getItem('token');
      if (token && !username) {
        const response = await fetch(`${API_URL}/api/users/profile`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        const data = await response.json();
        setUsername(data.username);
      }
    };
    fetchUserProfile();
  }, [username]);

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
          <Text style={styles.welcomeText}>Welcome back, {username}!</Text>
          <Text style={styles.subHeaderText}>Here are your saved and books!</Text>
        </View>
        <SearchBar
          style={styles.searchBar}
          placeholder="Search here"
          onPress={() => alert("onPress")}
          onChangeText={(text) => console.log(text)}
        />

        <BookList 
          books={savedBooks} 
          onBookPress={(book) => console.log(`Selected book: ${book.title}`)}  // Handle book press
        />

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
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default SavedBooksScreen;
