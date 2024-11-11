import React, { useContext, useEffect, useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';
import { View, Text, ScrollView, StyleSheet, ActivityIndicator, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import SearchBar from "react-native-dynamic-search-bar";
import { SavedBooksContext } from '../contexts/SavedBooksContext';
import { UserContext } from '../contexts/UserContext';
import BookList from '../components/BookList';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useNavigation } from '@react-navigation/native';

const SavedBooksScreen = () => {
  const { savedBooks, loading } = useContext(SavedBooksContext);
  const { username, fetchUserProfile } = useContext(UserContext);
  const navigation = useNavigation();
  const [searchTerm, setSearchTerm] = useState('');

  useEffect(() => {
    if (!username) {
      fetchUserProfile();
    }
  }, [username]);

 
  const filteredBooks = savedBooks.filter(book => 
    book.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const clearSearch = () => {
    setSearchTerm('');
  };

  if (loading) {
    return (
      <View style={styles.loadingContainer}>
        <ActivityIndicator size="large" color="#0000ff" />
      </View>
    );
  }

  return (
    <SafeAreaView style={styles.safeArea}>
    <View style={styles.outerContainer}>
      <View style={styles.scrollContainer}>
        <View style={styles.header}>
          <Ionicons 
              name="menu" 
              size={32} color="black" 
              style={styles.menuIcon} 
              onPress={() => navigation.toggleDrawer()}
             />
          <View style={styles.circleIcon}></View>
        </View>
        <View style={styles.headerTextContainer}>
          <Text style={styles.welcomeText}>{username ? `Welcome back, ${username}!` : 'Welcome back!'}</Text>
          <Text style={styles.subHeaderText}>Here are your saved books!</Text>
        </View>
        <SearchBar
          style={styles.searchBar}
          placeholder="Search here"
          //onPress={() => alert("onPress")}
          onChangeText={(text) => setSearchTerm(text)}
          onClearPress={clearSearch}
        />

        <BookList 
          books={filteredBooks} 
          onBookPress={(book) => navigation.navigate('Description', {book})}
        />

      </View>
    </View>
    </SafeAreaView>
  );
};


/*
return (
    <SafeAreaView style={styles.safeArea}>
    <View style={styles.outerContainer}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.header}>
          <Ionicons 
              name="menu" 
              size={32} color="black" 
              style={styles.menuIcon} 
              onPress={() => navigation.toggleDrawer()}
             />
          <View style={styles.circleIcon}></View>
        </View>
        <View style={styles.headerTextContainer}>
          <Text style={styles.welcomeText}>{username ? `Welcome back, ${username}!` : 'Welcome back!'}</Text>
          <Text style={styles.subHeaderText}>Here are your saved books!</Text>
        </View>
        <SearchBar
          style={styles.searchBar}
          placeholder="Search here"
          //onPress={() => alert("onPress")}
          onChangeText={(text) => setSearchTerm(text)}
          onClearPress={clearSearch}
        />

        <BookList 
          books={filteredBooks} 
          onBookPress={(book) => navigation.navigate('Description', {book})}
        />

      </ScrollView>
    </View>
    </SafeAreaView>
  );
};

*/

const styles = StyleSheet.create({
  outerContainer: {
    flex: 1,
    backgroundColor: 'white',
  },
  safeArea: {
    flex: 1,
    backgroundColor: 'white',
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
