import React from 'react';
import { View, Text, Image, StyleSheet, Dimensions, TouchableOpacity, SafeAreaView } from 'react-native';
import image from '../images/Study.png';
import dots from '../images/dots.png'

const { width, height } = Dimensions.get('window');

const ChooseLoginSignUpScreen = ({navigation}) => {
  return (
    <SafeAreaView style={styles.container}>
     <View style={styles.imageContainer}>
        <Image
          source={image}
          style={styles.image}
          resizeMode="contain" // Ensures image scales properly
        />
      </View>
      <Image
          style={styles.dotsStyle}
          source={dots}
          resizeMode="contain" // Ensures image scales properly
        />
      <View style={styles.bottomContainer}>
        <Text style={styles.title}>Find New Books</Text>
        <Text style={styles.description}>
          We use machine learning to provide you with new books and academic articles based on your preferences!
        </Text>
      </View>
      <View>
        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Login')}>
          <Text style={styles.buttonText}>Sign In</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('SignUp')}>
          <Text style={styles.buttonText}>Sign Up</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center', 
    padding: 16
  },
  bottomContainer: {
    marginTop: height * .05,
    width: width * .8
  },
  imageContainer: {
    width: '80%',
    aspectRatio: 1,      // Maintain aspect ratio for square image
    justifyContent: 'center',
    alignItems: 'center',
    maxWidth: width * 0.8,  // Ensure it doesn't exceed 70% of screen width
    maxHeight: height * 0.5, // Ensure it doesn't exceed half the screen height
  },
  image: {
    width: '100%',
    height: '100%',
  },
  dotsStyle: {
    marginTop: height * .03
  },
  title: {
    fontSize: 20,
    fontWeight: '600',
    marginBottom: 10,
    textAlign: 'center',
    color: '#19191B'
  },
  description: {
    textAlign: 'center',
    fontSize: 16,
    marginBottom: 20,
    color: '#9D9D9D'
  },
  button: {
    backgroundColor: '#C75550',
    paddingVertical: 15,
    paddingHorizontal: 50,
    borderRadius: 10,
    marginVertical: 5,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default ChooseLoginSignUpScreen;