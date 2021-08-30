import React from 'react';
import { StyleSheet, FlatList, ActivityIndicator, View, Text } from 'react-native';
import TreeListItem from '../components/TreeListItem';
import axios from 'axios';
import AsyncStorage from '@react-native-community/async-storage';

export default class Trees extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      trees: [],
      dataLoaded: false,
      loading: true,
    };
  }
  async componentDidMount() {
    const loggedIn = await AsyncStorage.get("loggedIn");
    if (!JSON.parse(loggedIn)) {
      this.props.navigation.navigate("Login");
    }
    this.setState({
      loading: false
    })
  }
  async doLogout() {
    try {
      await AsyncStorage.setItem("loggedIn", "false");
      await AsyncStorage.removeItem("username");
      await AsyncStorage.removeItem("password");
      
      this.props.navigation.navigate("Login");

    } catch(err) {
      console.log(err);
    }
    
  }
  async componentDidMount() {
    const { navigation } = this.props;
    try {
      navigation.setOptions({
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
      })
      const username = await AsyncStorage.getItem("username");
      const password = await AsyncStorage.getItem("password");
      
      const data = await axios.get('https://plantinum-stage.herokuapp.com/plants_with_data', {
        auth: {
          username: username,
          password: password
        }
      });
      this.setState({ 
        trees: data.data,
        dataLoaded: true
      });

    } catch (err) {
      console.warn(err, "trees");
    }
  }
  render() {
    const { navigation } = this.props;
    const { trees, dataLoaded, loading } = this.state;
    return (
      <View 
        style={
          !dataLoaded ? {height: "100%"} : {height: "100%",backgroundColor: "#58B0AE"}}
        >
        {( dataLoaded ) ? 
          (<FlatList 
            data={trees}
            renderItem={({ item }) => 
            <TreeListItem tree={item}
              onPress={() => navigation.navigate('Info', {
                type: item.type,
                latest_data: item.latest_data
              })}
            />}
            keyExtractor={item => `${item.id}`}
            contentContainerStyle={styles.container}
          />)
          : (<ActivityIndicator size="large" style={styles.loading}/>)
        }
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    paddingTop: 16,
    paddingHorizontal: 16,
    backgroundColor: "#58B0AE",
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
