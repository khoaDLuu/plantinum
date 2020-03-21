import React from 'react';
import { StyleSheet, ActivityIndicator } from 'react-native';
// import {Font} from 'expo';
import * as Font from 'expo-font';

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import Tree from './screens/TreeInformation';
import Trees from './screens/Trees';

const Stack = createStackNavigator();

export default class App extends React.Component {
  
  constructor(){
    super();
    this.state={
      fontLoaded: false
    }
  }
  async componentDidMount() {
    await Font.loadAsync({
      Gothic: require('./assets/fonts/SHOWG.ttf')
    });

    this.setState({ fontLoaded: true });
  }

  render() {

    return (
      <NavigationContainer >
        {this.state.fontLoaded ? (
        <Stack.Navigator>
          <Stack.Screen name="Home" component={Trees} />
          <Stack.Screen name="Home2" component={Tree} 
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
    flex: 1,
    justifyContent: "center",
    alignItems: "center"
  }
});
