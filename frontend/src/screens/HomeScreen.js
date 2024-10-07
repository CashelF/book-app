import React from 'react';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import SavedBooksScreen from './SavedBooksScreen';
import SwipingScreen from './SwipingScreen';
import { createMaterialBottomTabNavigator } from 'react-native-paper/react-navigation';

const Tab = createMaterialBottomTabNavigator();
//const Tab = createMaterialTopTabNavigator();
//const Tab = createBottomTabNavigator();

const HomeScreen = () => {
  return (
    <Tab.Navigator>
      <Tab.Screen name="Swiping" component={SwipingScreen} />
      <Tab.Screen name="Saved Books" component={SavedBooksScreen} />
    </Tab.Navigator>
  );
};

export default HomeScreen;
