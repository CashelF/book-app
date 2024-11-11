import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import LoginScreen from './screens/LoginScreen';
import SignUpScreen from './screens/SignUpScreen';
import HomeScreen from './screens/HomeScreen';
import UserInfoScreen from './screens/UserInfoScreen';
import ChooseLoginSignUpScreen from './screens/ChooseLoginSignUpScreen';
import ReadingHistoryScreen from './screens/ReadingHistoryScreen';
import { LikedBooksProvider } from './contexts/LikedBooksContext';
import { SavedBooksProvider } from './contexts/SavedBooksContext';
import { UserProvider } from './contexts/UserContext';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import BookDescriptionScreen from './screens/BookDescriptionScreen';
import DrawerNavigation from './screens/DrawerNavigation';
const Stack = createStackNavigator();

function App() {
  return (
    <SafeAreaProvider>
    <LikedBooksProvider>
      <SavedBooksProvider>
        <UserProvider>
          <NavigationContainer>
            <Stack.Navigator initialRouteName="ChooseLoginSignUpScreen">
              <Stack.Screen 
                name="Login" 
                component={LoginScreen} 
                options={{ headerShown: false }} 
              />
              <Stack.Screen 
                name="SignUp" 
                component={SignUpScreen} 
                options={{ headerShown: false }} 
              />
              <Stack.Screen 
                name="UserInfo" 
                component={UserInfoScreen} 
                options={{ headerShown: false }} 
              />
              <Stack.Screen 
                name="ReadingHistory" 
                component={ReadingHistoryScreen} 
                options={{ headerShown: false }} 
              />
              <Stack.Screen 
                name="Home" 
                component={HomeScreen} 
                options={{ headerShown: false }} 
              />
              <Stack.Screen 
                name="ChooseLoginSignUpScreen" 
                component={ChooseLoginSignUpScreen} 
                options={{ headerShown: false }} 
              />
              <Stack.Screen
                name="Description"
                component={BookDescriptionScreen}
                options={{headerShown: false}}
              />
              <Stack.Screen 
                  name="HomeDrawer" 
                  component={DrawerNavigation} 
                  options={{ headerShown: false }} 
                />
            </Stack.Navigator>
          </NavigationContainer>
        </UserProvider>
      </SavedBooksProvider>
    </LikedBooksProvider>
    </SafeAreaProvider>
  );
}

export default App;
