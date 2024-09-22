import React, { createContext, useState } from 'react';

export const UserContext = createContext();

export const UserProvider = ({ children }) => {
  const [username, setUsername] = useState(null);

  const fetchUserProfile = async () => {
    const token = await AsyncStorage.getItem('access_token');
    if (token && !username) {
      const response = await fetch(`${API_URL}/api/users/profile`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();
      setUsername(data.username);
    }
  };

  return (
    <UserContext.Provider value={{ username, setUsername, fetchUserProfile }}>
      {children}
    </UserContext.Provider>
  );
};
