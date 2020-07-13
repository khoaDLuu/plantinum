import React from 'react';
import { StyleSheet, ActivityIndicator, Text } from 'react-native';
// import {Font} from 'expo';
import * as Font from 'expo-font';

import AsyncStorage from '@react-native-community/async-storage';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import {decode, encode} from 'base-64';

if (!global.btoa) {
    global.btoa = encode;
}

if (!global.atob) {
    global.atob = decode;
}

import Tree from './screens/TreeInformation';
import Trees from './screens/Trees';
import LoginPage from './screens/Login';

const Stack = createStackNavigator();



export default class App extends React.Component {
  
  constructor() {
    super();
    this.state={
      isLogged: false,
      loading: true
    }
  }
  async componentDidMount() {
    try {
      await Font.loadAsync({
        Gothic: require('./assets/fonts/SHOWG.ttf')
      });
      const loggedIn = await AsyncStorage.getItem('loggedIn');
      this.setState({
        loggedIn: JSON.parse(loggedIn),
        loading: false
      });
    } catch(err) {
      console.warn(err, "App");
    }
  }
  async doLogout() {
    try {
      await AsyncStorage.setItem("loggedIn", "false");
      await AsyncStorage.removeItem("username");
      await AsyncStorage.removeItem("password");
      this.setState({
        loggedIn: false
      });

    } catch(err) {
      console.log(err);
    }
    
  }

  render() {
    const { loading, loggedIn } = this.state;
    console.log(loggedIn);
    return (
      <NavigationContainer  >
        {!loading ? (
        <Stack.Navigator>
          <Stack.Screen name="Login" component={LoginPage} />
          <Stack.Screen 
            name="Home" 
            component={Trees}
            options={{
              headerLeft: null,
              headerRight: () => {
                return (<Text
                  style={styles.logout}
                  onPress={() =>  {this.doLogout();
                    alert("Logout");
                  }}
                >
                  Logout
                </Text>);
              }
            }}    
         />
          <Stack.Screen name="Info" component={Tree} 
            options={({route}) => {return {title: route.params.treeName}}} 
          />
          
        </Stack.Navigator>
        ) : (<ActivityIndicator size="large" style={styles.loading} />
        )}
        </NavigationContainer> 
    
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    justifyContent: 'center',
    alignItems: 'stretch',
    // paddingHorizontal: 16,
    marginHorizontal: 16
  },
  loading: {
    height: "80%",
    flex: 1,
    justifyContent: "center",
    alignItems: "center"
  },
  logout: {
    color: "#a31515",
    padding: 10
  }
});
