import React from 'react';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { Ionicons } from '@expo/vector-icons';
import SavedBooksScreen from './SavedBooksScreen';  // Import the screen

const Drawer = createDrawerNavigator();

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