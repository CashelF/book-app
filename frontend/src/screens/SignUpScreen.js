import React, { useState, useContext } from 'react';
import { View, Text, Button, TouchableOpacity, StyleSheet, Alert, Dimensions } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { API_URL } from '@env';
import { UserContext } from '../contexts/UserContext';
import { PaperProvider, TextInput } from 'react-native-paper';
import { SocialIcon } from '@rneui/themed';
import { Ionicons } from '@expo/vector-icons';

const { width } = Dimensions.get('window');
const { height } = Dimensions.get('window');
const calculateFontSize = () => {
  if (width < 360) {
    return 32; // Small devices
  } else if (width < 768) {
    return 40; // Medium devices
  } else {
    return 40; // Large devices
  }
};

export default function SignUpScreen({ navigation }) {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const { setUsername: setGlobalUsername } = useContext(UserContext);

  const handleSignUp = async () => {
    try {
      const response = await fetch(`${API_URL}/api/auth/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
      });
      const result = await response.json();
      if (response.status === 201) {
        Alert.alert('Registration Successful', 'Welcome!');
        await AsyncStorage.setItem('access_token', result.access_token);
        setGlobalUsername(username);
        navigation.navigate('UserInfo');
      } else {
        Alert.alert('Registration Failed', result.message || 'An error occurred');
      }
    } catch (error) {
      Alert.alert('Registration Error', 'An error occurred');
    }
  };

  return (
    <PaperProvider>
    <View style={styles.container}>
      <View style={styles.backButtonView}>
        <TouchableOpacity onPress={() => navigation.navigate('ChooseLoginSignUpScreen')}>
          <Ionicons 
                  name="arrow-back-outline" 
                  size={30} 
                  color={"#19191B"}
                  
                  />
          </TouchableOpacity>
      </View>
      <View>
        <View style={styles.titleContainer}>
          <Text style={styles.title}>Create Your</Text>
          <Text style={styles.title}>Account</Text>
        </View>
        <TextInput
          style={styles.input}
          textColor='#938B8B'
          placeholder="Username"
          placeholderTextColor={'#938B8B'}
          underlineColor="transparent"
          activeUnderlineColor="transparent"
          mode='flat'
          keyboardType="email-address"
          value={email}
          onChangeText={setUsername}
          left={<TextInput.Icon icon="account" style={styles.icon} color={'#938B8B'}/>}
        />
        <TextInput
          style={styles.input}
          textColor='#938B8B'
          placeholder="Email"
          placeholderTextColor={'#938B8B'}
          underlineColor="transparent"
          activeUnderlineColor="transparent"
          mode='flat'
          keyboardType="email-address"
          value={email}
          onChangeText={setEmail}
          left={<TextInput.Icon icon="email" style={styles.icon} color={'#938B8B'}/>}
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          placeholderTextColor={'#938B8B'}
          textColor='#938B8B'
          underlineColor="transparent"
          activeUnderlineColor="transparent"
          mode='flat'
          secureTextEntry
          value={password}
          onChangeText={setPassword}
          left={<TextInput.Icon icon="lock" color={'#938B8B'}/>}
          right={<TextInput.Icon icon="eye" color={'#938B8B'}/>}
        />
      <TouchableOpacity onPress={handleSignUp} style={styles.signInButtonContainer}>
        <Text style={styles.signInButtonText}>Create Account</Text>
      </TouchableOpacity>
      <View style={styles.socialContainer}>
        <Text style={styles.continueWithText}>or continue with</Text>
        <View style={styles.socialButtons}>
        <SocialIcon
          type='facebook'
        />
          <SocialIcon
            type='google'
          />
          <SocialIcon
            type='linkedin'
          />
        </View>
      </View>
      </View>
      <View style={styles.signUpTextContainer}>
        <Text style={styles.dontHaveAccountText}>Already Have An Account? {' '}</Text>
        <TouchableOpacity onPress={() => navigation.navigate('Login')}>
          <Text style={styles.link}> Login</Text>
        </TouchableOpacity>
      </View>
    </View>
    </PaperProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 16,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'space-around'
  },
  backButtonView: {
    width: width * .8,
  },
  signUpTextContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  continueWithText: {
    color: '#837F7F',
    fontSize: 16
  },
  dontHaveAccountText: {
    color: '#CCBEBE',
    fontSize: 14
  },
  icon: {
    marginRight: 2
  },
  signInButtonContainer: {
    backgroundColor: '#D45555', 
    borderRadius: 50,
    overflow: 'hidden', 
    width: width * .8,
    padding: 20,
    alignItems: 'center',
    justifyContent: 'center',
    text: 'white',
    marginTop: 20,
  },
  signInButtonText: {
    color: 'white',
    fontSize: 16
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
  input: {
    height: 40,
    color: 'black',
    marginBottom: 12,
    padding: 10,
    borderWidth: 0,
    width: width * .8,
    paddingVertical: 2,
    backgroundColor: '#F8F8F8',
    borderRadius: 5
  },
  testbutton: {
    width: width * .8
  },
  link: {
    color: '#D45555',
    fontWeight: 'bold',
    fontSize: 18
  },
  forgot: {
    color: '#FF5A5F',
    marginTop: 10,
    textAlign: 'center',
  },
  socialContainer: {
    alignItems: 'center',
    width: width * .8,
    marginTop: 20,
  },
  socialButtons: {
    flexDirection: 'row',
    justifyContent: 'center',
    width: '100%',
    maxWidth: 400,
    marginTop: 10,
  },
  socialButton: {
    width: 50,
    height: 50,
    backgroundColor: '#ccc',
    borderRadius: 25,
    marginHorizontal: 10,
  },
});

