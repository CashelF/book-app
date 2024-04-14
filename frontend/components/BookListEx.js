
import React from 'react';
import { FlatList, View, Text, StyleSheet, Image } from 'react-native';

const books = [
  { id: '1', title: 'Catcher in the Rye', author: 'J.D. Salinger'},
  { id: '2', title: 'Great Expectations', author: 'Charles Dickens'},
  { id: '3', title: 'My Sister’s Keeper', author: 'Jodi Picoult'},
  { id: '4', title: 'Someone Like You', author: 'Roald Dahl' },
  { id: '5', title: 'My Sister’s Keeper', author: 'Jodi Picoult'},
  { id: '6', title: 'Someone Like You', author: 'Roald Dahl' },
  { id: '7', title: 'My Sister’s Keeper', author: 'Jodi Picoult'},
  { id: '8', title: 'Someone Like You', author: 'Roald Dahl' },
];

"<Image source={imageUrl} style={styles.bookImage} />"
const BookItem = ({ title, author, imageUrl }) => (
  <View style={styles.bookItem}>
    <View style={styles.bookImage} />
    <Text style={styles.bookTitle}>{title}</Text>
    <Text style={styles.bookAuthor}>{author}</Text>
  </View>
);

const BookGrid = () => {
  return (
    <FlatList
      data={books}
      renderItem={({ item }) => (
        <BookItem
          title={item.title}
          author={item.author}
          imageUrl={item.imageUrl}
        />
      )}
      keyExtractor={(item) => item.id}
      numColumns={2}
      columnWrapperStyle={styles.row}
      showsVerticalScrollIndicator={true}
      contentContainerStyle={{
        paddingBottom: 500, 
      }}
    />
  );
};

const styles = StyleSheet.create({
  bookItem: {
    flex: 1,
    borderRadius: 8,
    overflow: 'hidden',
    backgroundColor: '#fff',
    elevation: 3,
    shadowOffset: { width: 1, height: 1 },
    shadowColor: 'black',
    shadowOpacity: 0.3,
    shadowRadius: 2,
    marginHorizontal: 7.5,
  },
  bookImage: {
    width: '100%',
    height: 250,
    resizeMode: 'cover',
    backgroundColor: '#D45555',
    borderRadius: 20
  },
  bookTitle: {
    fontWeight: 'bold',
    fontSize: 16,
    margin: 10,
  },
  bookAuthor: {
    fontSize: 14,
    marginBottom: 10,
    marginHorizontal: 10,
  },
  row: {
    justifyContent: 'space-between',
    paddingHorizontal: 15,
  },
});

export default BookGrid;