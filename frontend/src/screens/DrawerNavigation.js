import React from 'react';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { Ionicons } from '@expo/vector-icons';
import SavedBooksScreen from './SavedBooksScreen';  // Import the screen
import { NavigationContainer } from '@react-navigation/native';
import HomeScreen from './HomeScreen'
import LoginScreen from './LoginScreen';

const Drawer = createDrawerNavigator();

export default function DrawerNavigation() {
  return (
      <Drawer.Navigator initialRouteName="SavedBooks"
      screenOptions={{
        headerShown: false, // Hide the drawer's top header
        drawerType: 'slide', // You can choose different types: 'front', 'back', 'slide'
      }}>
       <Drawer.Screen name="Account Screen" component={HomeScreen} />
       <Drawer.Screen name="Logout" component={LoginScreen} />
      </Drawer.Navigator>
  );
}

/*
<Drawer.Screen name="SavedBooks" component={SavedBooksScreen} />
const DrawerNavigator = () => {
  return (
    <Drawer.Navigator
      initialRouteName="SavedBooks"
      screenOptions={{
        drawerStyle: {
          backgroundColor: '#f8f8f8',
          width: 240,
        },
        headerShown: false,  // Hide header if not needed
        drawerActiveTintColor: '#D45555',
        drawerInactiveTintColor: '#000',
      }}
    >
      <Drawer.Screen 
        name="SavedBooks" 
        component={SavedBooksScreen} 
        options={{
          drawerLabel: 'Saved Books',
          drawerIcon: ({ color, size }) => (
            <Ionicons name="bookmarks" size={size} color={color} />
          ),
        }} 
      />
    </Drawer.Navigator>
  );
};

export default DrawerNavigator;
*/