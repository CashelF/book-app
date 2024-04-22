import React from 'react';
import { View, Text, Button, Image,TouchableOpacity, StyleSheet } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import SearchBar from "react-native-dynamic-search-bar";
import BookGrid from '../components/BookListExV2';

const bookIdList1 = ['Ar1jswEACAAJ','-AfkybBr0ooC','ydQiDQAAQBAJ','sI_UG8lLey0C','WzbyEAAAQBAJ','Iu_BAgAAQBAJ','JOgBAAAAYAAJ','N-RSlCrhrpEC'];
const bookIdList2 = ['EoA7AQAAMAAJ','dbr_9Ff5rOcC','y-37CgAAQBAJ','h4cwEAAAQBAJ','8XwmDwAAQBAJ','Coi9AwAAQBAJ', '9YEOAAAAIAAJ','FFTJDYx_ZiEC'];

const HomeScreen = () => {
    return (
        <View style={styles.everythingContainer}>
            <View style={styles.container}>
            <View style={styles.menuContainer}>
            <Ionicons name="menu" size={32} color="black" style={styles.menuIcon} />
            <View style={styles.circleIcon}></View>
            </View>
            <View style={styles.header}>
            <Text style={styles.welcomeText}>Welcome back, Bunny!</Text>
            <Text style={styles.subHeaderText}>Here are your saved and suggested books!</Text>
            </View>
            <SearchBar
                style={styles.searchBar}
                placeholder="Search here"
                onPress={() => alert("onPress")}
                onChangeText={(text) => console.log(text)}
            />
            <View style={styles.buttonLayout}>
                <TouchableOpacity style={{height:50,backgroundColor:"white",alignItems:'center',justifyContent:'center', paddingRight: 10}}>
                    <Text style={{fontSize:16,}}>Saved</Text>
                </TouchableOpacity>
                <TouchableOpacity style={{height:50,backgroundColor:"white",alignItems:'center',justifyContent:'center'}}>
                    <Text style={{fontSize:16,}}>Suggested</Text>
                </TouchableOpacity>
            </View> 
            </View>
            <BookGrid bookIds={bookIdList1} />
            </View>
    );
};

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
  circleIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: 'black', 
  },
  welcomeText: {
    color: "#9D9D9D",
    fontSize: 16
  },
  subHeaderText: {
    color: "#19191B",
    fontSize: 26
  },
  searchBar: {
    width: "100%",
    marginTop: 20,
    backgroundColor: 'rgba(196, 196, 196, 0.15)'
  },
  buttonLayout: {
    display: 'flex',
    flexDirection: 'row',
    marginTop: 10
  },
});

export default HomeScreen;
