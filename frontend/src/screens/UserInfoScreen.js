import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert, Dimensions } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import { API_URL } from '@env';
import { PaperProvider, TextInput } from 'react-native-paper';
import { SocialIcon } from '@rneui/themed';
import { Ionicons } from '@expo/vector-icons';


const { width, height } = Dimensions.get('window');

const calculateFontSize = () => {
  if (width < 360) {
    return 32; // Small devices
  } else if (width < 768) {
    return 40; // Medium devices
  } else {
    return 40; // Large devices
  }
};

const UserInfoScreen = ({ navigation }) => {
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');

  const handleNext = async () => {
    if (age && gender) {
      try {
        const token = await AsyncStorage.getItem('access_token');
        const response = await axios.post(
          `${API_URL}/api/users/profile`,
          { age, gender },
          {
            headers: {
              Authorization: `Bearer ${token}`,
              'Content-Type': 'application/json',
            },
          }
        );
        if (response.status === 200) {
          navigation.navigate('ReadingHistory');
        }
      } catch (error) {
        console.error('Error updating user info:', error);
        Alert.alert('Error updating user info. Please try again.');
      }
    } else {
      Alert.alert('Please fill in all fields.');
    }
  };



  return (
    <PaperProvider>
    <View style={styles.container}>
      <View style={styles.titleContainer}>
          <Text style={styles.title}>Tell us about</Text>
          <Text style={styles.title}>yourself</Text>
      </View>
      <View>
        <TextInput
          style={styles.input}
          placeholder="Age"
          keyboardType="numeric"
          underlineColor="transparent"
          activeUnderlineColor="transparent"
          mode='flat'
          textColor='#938B8B'
          value={age}
          onChangeText={setAge}
          left={<TextInput.Icon icon="duck" style={styles.icon} color={'#938B8B'}/>}
        />
        <Text style={styles.subtitle}>Gender</Text>
        <View style={styles.genderContainer}>
          <TouchableOpacity
            style={[
              styles.genderButton,
              gender === 'male' && styles.genderButtonSelected,
            ]}
            onPress={() => setGender('male')}
          >
            <Text style={[
                    styles.genderButtonText, // Default text style
                    { color: gender === 'male' ? '#fff' : 'black' } // Change text color based on gender
                  ]}
            >
                Male
             </Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[
              styles.genderButton,
              gender === 'female' && styles.genderButtonSelected,
            ]}
            onPress={() => setGender('female')}
          >
            <Text style={[
                    styles.genderButtonText, // Default text style
                    { color: gender === 'female' ? '#fff' : 'black' } // Change text color based on gender
                  ]}
            >Female</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[
              styles.genderButton,
              gender === 'other' && styles.genderButtonSelected,
            ]}
            onPress={() => setGender('other')}
          >
            <Text style={[
                    styles.genderButtonText, // Default text style
                    { color: gender === 'other' ? '#fff' : 'black' } // Change text color based on gender
                  ]}
            >Other</Text>
          </TouchableOpacity>
        </View>
      </View>
      <TouchableOpacity style={styles.button} onPress={handleNext}>
        <Text style={styles.buttonText}>Next</Text>
      </TouchableOpacity>
    </View>
    </PaperProvider>
  );
};

const screenWidth = Dimensions.get('window').width;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: 'white',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  subtitle: {
    fontSize: 18,
    marginBottom: 10,
    alignSelf: 'center'
  },
  input: {
    height: 40,
    color: 'black',
    marginBottom: 12,
    padding: 10,
    borderWidth: 0,
    //width: screenWidth > 600 ? '50%' : '100%',
    width: width * .8,
    paddingVertical: 2,
    backgroundColor: '#F8F8F8',
    borderRadius: 5
  },
  genderContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    //width: screenWidth > 600 ? '50%' : '100%',
    width: width * .8,
    marginVertical: 10,
  },
  titleContainer: {
    width: width * .8,
    alignItems: 'flex-start',
    marginBottom: height * .05
  },
  title: {
    fontSize: calculateFontSize(),
    fontWeight: 'bold',
  },
  genderButton: {
    flex: 1,
    padding: 10,
    marginHorizontal: 5,
    //borderColor: '#ccc',
    borderColor: '#DCD3D3',
    borderWidth: 1,
    borderRadius: 50,
    alignItems: 'center',
  },
  genderButtonSelected: {
    backgroundColor: '#D45555',
    borderWidth: 0
  },
  genderButtonText: {
    color: 'black',
  },
  button: {
    marginTop: 20,
    padding: 15,
    backgroundColor: '#D45555',
    borderRadius: 50,
    //width: screenWidth > 600 ? '50%' : '100%',
    width: width * .8,
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
  },
});

export default UserInfoScreen;
