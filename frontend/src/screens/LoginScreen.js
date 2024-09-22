import React, { useState, useContext } from 'react';
import { View, Text, TextInput, Button, TouchableOpacity, StyleSheet, Alert, Dimensions } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { UserContext } from '../contexts/UserContext';
import { SavedBooksContext } from '../contexts/SavedBooksContext';
import { LikedBooksContext } from '../contexts/LikedBooksContext';
import { API_URL } from '@env';

const { width } = Dimensions.get('window');

export default function LoginScreen({ navigation }) {
  const { setUsername } = useContext(UserContext);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { fetchSavedBooks } = useContext(SavedBooksContext);
  const { fetchLikedBooks } = useContext(LikedBooksContext);

  const handleLogin = async () => {
    try {
      const response = await fetch(`${API_URL}/api/auth/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });
      const result = await response.json();
      if (response.ok) {
        await AsyncStorage.setItem('access_token', result.access_token);
        await fetchSavedBooks();
        await fetchLikedBooks();
        setUsername(result.username);
        navigation.navigate('Home');
      } else {
        Alert.alert('Login Failed', result.message || 'An error occurred');
      }
    } catch (error) {
      Alert.alert('Login Error', 'An error occurred');
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login to your Account</Text>
      <TextInput
        style={styles.input}
        placeholder="Email"
        keyboardType="email-address"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={setPassword}
      />
      <Button title="Sign In" onPress={handleLogin} color="#FF5A5F" />
      <TouchableOpacity onPress={() => navigation.navigate('SignUp')}>
        <Text style={styles.link}>Don't have an account? Sign up</Text>
      </TouchableOpacity>
      <TouchableOpacity>
        <Text style={styles.forgot}>Forgot password?</Text>
      </TouchableOpacity>
      <View style={styles.socialContainer}>
        <Text>or continue with</Text>
        <View style={styles.socialButtons}>
          <View style={styles.socialButton} />
          <View style={styles.socialButton} />
          <View style={styles.socialButton} />
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 16,
    backgroundColor: '#fff',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    height: 40,
    borderColor: '#ccc',
    borderWidth: 1,
    marginBottom: 12,
    padding: 10,
    borderRadius: 5,
    width: '80%',
    maxWidth: 400,
  },
  link: {
    color: '#FF5A5F',
    marginTop: 10,
  },
  forgot: {
    color: '#FF5A5F',
    marginTop: 10,
    textAlign: 'center',
  },
  socialContainer: {
    alignItems: 'center',
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
