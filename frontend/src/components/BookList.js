import React from 'react';
import { View, Text, FlatList, TouchableOpacity, Image, StyleSheet, Dimensions } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const BookList = ({ books, onBookPress, selectedBooks }) => {
  const screenWidth = Dimensions.get('window').width;

  return (
    <FlatList
      contentContainerStyle={styles.bookList}
      data={books}
      keyExtractor={(item) => item.id.toString()}
      renderItem={({ item }) => (
        <TouchableOpacity style={styles.bookItem} onPress={() => onBookPress(item)}>
          <Image style={styles.bookImage} source={{ uri: item.cover_image_url }} />
          {selectedBooks && selectedBooks.includes(item.id) && (
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
  );
};

const screenWidth = Dimensions.get('window').width;

const styles = StyleSheet.create({
  bookList: {
    paddingBottom: 80,
  },
  bookItem: {
    width: (screenWidth / 2) - 30,
    marginHorizontal: 10,
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
    top: 5,
    right: 30,
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
  fixedHeightList: {
    height: 400,
  },
});

export default BookList;
