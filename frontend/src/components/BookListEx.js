
import React, { useEffect, useState } from 'react';
import { FlatList, View, Text, StyleSheet, Image, TouchableOpacity, ScrollView} from 'react-native';
import Modal from 'react-native-modal';
import axios from 'axios';

const BookDes = ({ isPageVisible, children }) => {
  return (
    <Modal isVisible={isPageVisible} /*animationType="fade"*/ >
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <View style={{ backgroundColor: 'white', padding: 20, borderRadius: 10 }}>
          {children}
        </View>
      </View>
    </Modal>
  );
};

const BookItem = ({ title, author, imageUrl, description }) => {
  const [isPageVisible, setIsPageVisible] = React.useState(false);

  const pageToggle = () => setIsPageVisible(() => !isPageVisible);

  return (
    <View style={styles.bookItem}>
      <BookDes isPageVisible={isPageVisible}>
        <View style={styles.bookItem}>
          <TouchableOpacity onPress={pageToggle} style={{ marginTop: 10 }}>
            <Text style={styles.bookTitle}>{title}</Text>
            <Text style={styles.bookAuthor}>      by {author}</Text>
          </TouchableOpacity>
          <ScrollView>
          <Text style={styles.bookAuthor}>{description}</Text>
          </ScrollView>
        </View>
      </BookDes>
      <TouchableOpacity onPress={pageToggle}>
        <Image source={{uri:imageUrl}} style={styles.bookImage} />
      </TouchableOpacity>
      <Text style={styles.bookTitle}>{title}</Text>
      <Text style={styles.bookAuthor}>{author}</Text>
    </View>
  );
};

const BookGrid = ({ bookIds }) => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    const fetchBooks = async () => {
      var bookList = [];
      const bookIdsParam = bookIds.join('|');
      for(var i = 0; i < bookIds.length; i++){
        const response = await axios.get(`https://www.googleapis.com/books/v1/volumes/${bookIds[i]}`);
        bookList.push(response.data);
      }
      setBooks(bookList);
    };

    if (bookIds.length > 0) {
      fetchBooks();
    }
  }, [bookIds]);
  

  return (
    <FlatList
      data={books}
      renderItem={({ item }) => (
        <BookItem
          title={item.volumeInfo.title}
          author={item.volumeInfo.authors[0]}
          imageUrl={item.volumeInfo.imageLinks.thumbnail}
          description={item.volumeInfo.description}
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