import React from 'react';
import { View, StyleSheet, Dimensions } from 'react-native';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import SavedBooksScreen from './SavedBooksScreen';
import SwipingScreen from './SwipingScreen';
import { createMaterialBottomTabNavigator } from 'react-native-paper/react-navigation';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';

const Tab = createMaterialBottomTabNavigator();
const { width, height } = Dimensions.get('window');
//const Tab = createMaterialTopTabNavigator();
//const Tab = createBottomTabNavigator();

const HomeScreen = () => {
  return (
    <View style={styles.container}>
    <Tab.Navigator
      barStyle={{
        backgroundColor: '#F8F8F8',
        borderTopLeftRadius: 50,     
        borderTopRightRadius: 50,  
        overflow: 'hidden',
      }}
    >
       <Tab.Screen name="Saved Books" 
      component={SavedBooksScreen} 
        options={{
          tabBarLabel: 'Saved Books',
          tabBarIcon: () => {
            return <Ionicons name="home" size={24} color="#D45555" />;
          }
        }}
      />
      <Tab.Screen 
        name="Swiping" 
        component={SwipingScreen} 
        options={{
          tabBarLabel: 'Swiping',
          tabBarIcon: () => {
            return <Ionicons name="heart" size={24} color="#D45555" />;
          }
        }}
      />
    </Tab.Navigator>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
  },
});


export default HomeScreen;
