import React, {useState, useContext} from 'react';
import { View, Text, Image, StyleSheet, Dimensions, ActivityIndicator, TouchableOpacity, ScrollView, SafeAreaView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import Entypo from '@expo/vector-icons/Entypo';
import { useNavigation } from '@react-navigation/native';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { SavedBooksContext } from '../contexts/SavedBooksContext';
import { API_URL } from '@env';

const { width } = Dimensions.get('window');

const BookDescriptionScreen = ({route}) => {
    const {book} = route.params;
    const navigation = useNavigation();
    console.log(book)
    const [isSaved, setIsSaved] = useState(true);
    const { savedBooks, setSavedBooks } = useContext(SavedBooksContext);
    const handleUnsaving = () => {
      // Your logic to handle unsaving
      console.log('Bookmark toggled');
      setIsSaved(prevState => !prevState); // Toggle the saved state
    };

    const handleSave = async () => {
      //const currentBook = books[currentIndex];
      const token = await AsyncStorage.getItem('access_token');
    
      try {
        if (isSaved) {
          await axios.post(`${API_URL}/api/interactions/unsave`, { book_id: book.id }, {
            headers: { Authorization: `Bearer ${token}` }
          });
          setSavedBooks(savedBooks.filter(b => b.id !== book.id));
          setIsSaved(false);
        } else {
          await axios.post(`${API_URL}/api/interactions/save`, { book_id: book.id }, {
            headers: { Authorization: `Bearer ${token}` }
          });
          setSavedBooks(savedBooks =>[...savedBooks, book]);
          setIsSaved(true);
        }
      } catch (error) {
        console.error('Error recording save interaction:', error);
      }
    };
    //  <TouchableOpacity onPress={() => navigation.navigate('Home', { screen: 'Saved Books' })}>
    return (
        <SafeAreaView>
          <View style={styles.topBar}>
          <TouchableOpacity onPress={() => navigation.goBack()}>
              <Ionicons 
                name="arrow-back-outline" 
                size={30} 
                color={"#19191B"}
              />
            </TouchableOpacity>
            <TouchableOpacity onPress={handleSave}>
              <Ionicons 
                name="bookmark" 
                size={30} 
                color={isSaved ? "#D45555": "#19191B"}
              />
            </TouchableOpacity>
          </View>
          <View style={styles.card}>
            {book.cover_image_url ? (
            <Image source={{ uri: book.cover_image_url }} style={styles.image} />
          ) : (
            <View style={styles.noImage}>
              <Text>No Image Available</Text>
            </View>
          )}
          <Text style={styles.title}>{book.title}</Text>
          <Text style={styles.subHeaderText}>Description</Text>
          <View style={styles.descriptionContainer}>
            <ScrollView>
              <Text style={styles.description}>{book.description}</Text>
            </ScrollView>
          </View>
        </View>
      </SafeAreaView>
    )
    };
          

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: '#fff',
    },
    topBar: {
      display: 'flex',
      flexDirection: 'row',
      justifyContent: 'space-between',
      padding: 20,
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

export default BookDescriptionScreen;