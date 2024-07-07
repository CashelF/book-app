import React from 'react';
import { View, Text, Button, Image,TouchableOpacity, StyleSheet, Pressable } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import Octicons from '@expo/vector-icons/Octicons';
import Entypo from '@expo/vector-icons/Entypo';
import SearchBar from "react-native-dynamic-search-bar";
import BookGrid from '../components/BookListEx'



const SwipingScreen = () => {

    function swipeNo() {
      console.log('No');
    }
    function swipeYes() {
        console.log('Yes');
    } 

    return (
        <View style={styles.container}>
            <View style={styles.menuContainer}>
                <Ionicons name="arrow-back-outline" size={32} color="black" style={styles.menuIcon} />
            </View>
            <View style={styles.centerContainer}>
                <View style={styles.bookImage}>
                </View>
                <Text style={styles.titleText} numberOfLines={1}>Cather in the Rye</Text>
                <Text style={styles.authorText} numberOfLines={1}>J.D Salinger</Text>
            </View>
            <View style={styles.bookInfo}>
                <Text style={styles.titleText}>Overview</Text>
                <Text style={styles.authorText} numberOfLines={6}>The Catcher in the Rye is a novel by J. D. Salinger, 
                  partially published in serial form in 1945–1946 
                  and as a novel in 1951. It was originally intended 
                  for adults but is often read by adolescents for its 
                  theme of angst, alienation and as a critique......
                </Text>
            </View>
            <View style={styles.swipingButtons}>
                <Pressable onPress={swipeNo}>
                  <Entypo name="circle-with-cross" size={72} color="#E94057" style={styles.swipeIcons}/>
                </Pressable>
                <Pressable onPress={swipeYes}>
                  <Ionicons name="heart-circle" size={72} color="green" />
                </Pressable>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: '#fff',
        justifyContent: 'flex-start',
        paddingTop: 70,
        paddingLeft: 30,
        paddingRight: 30
      },
      menuContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'space-between',
        marginBottom: 20,
      },
      centerContainer: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center'
      },
      bookImage: {
        width: '60%',
        height: 300,
        resizeMode: 'cover',
        backgroundColor: '#D45555',
        borderRadius: 20,
      },
      titleText: {
        marginTop: 10,
        color: '#19191B',
        fontSize: 16,
        fontWeight: 'bold'
      },
      authorText: {
        color: '#9D9D9D',
        marginTop: 5
      },
      bookInfo: {

      },
      swipingButtons: {
        marginTop: 20,
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'center'
      }

});

export default SwipingScreen;