import React from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity, ActivityIndicator } from 'react-native';

import AsyncStorage from '@react-native-community/async-storage';
import axios from 'axios';
import { ThemeColors } from 'react-navigation';

class LoginScreen extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      disable: false,
      loading: true
    }
  }
  async componentDidMount() {
    const loggedIn = await AsyncStorage.getItem("loggedIn");
    if (JSON.parse(loggedIn)) {
      this.props.navigation.navigate("Home");
    }
      this.setState({
        loading: false
      })
  }

  setValue(property, value) {
    this.setState({
      [property]: value
    });
  }

  async doLogin() {
    const { username, password } = this.state;
    if (!username || !password) {
      alert('Please type Username and Password');
      return;
    }

    this.setState({
      disable: true
    });
    try {
      const res = await axios.get("https://plantinum-stage.herokuapp.com/plants", {
        auth: {
          username: username,
          password: password
        }
      });    
        await AsyncStorage.setItem("username", username);
        await AsyncStorage.setItem("password", password);
        await AsyncStorage.setItem("loggedIn", "true");
        this.setState({
          disable: false
        });
        this.props.navigation.navigate("Home");
    } catch(err) {
      console.warn(err, "login");
      alert('Username or password is not correct');
    }
    
    
  }

  render() {
    const { username, password, disable, loading } = this.state;
    
    return (
      <View style={{height: "100%"}}>
      {
        loading ? <ActivityIndicator size="large" style={styles.loading} />
        :
        <View style={styles.container}>
        <View
          style={styles.formWrapper}
        >
          <Text
            style={styles.welcomeText}
          >
            Login
          </Text>
          <View style={styles.formRow}>
            <TextInput 
              style={styles.textInput}
              placeholder="Username"
              value={username}
              onChangeText={(value) => {
                this.setValue('username', value);
              }}
            />
          </View> 
          <View style={styles.formRow}>
            <TextInput 
              secureTextEntry={true}
              value={password}
              style={styles.textInput}
              placeholder="Password"
              onChangeText={(value) => {
                this.setValue('password', value);
              }}
            />
          </View>
        </View>
        <TouchableOpacity
          activeOpacity={0.8}
          style={ disable ? styles.disabledBtn : styles.signInBtn }
          onPress={() => this.doLogin()}
          disabled={disable}
        >
          <Text
            style={styles.signInText} 
          >
            { disable ? "Loading..." : "Sign in" }
          </Text>
        </TouchableOpacity>
        </View>
      }
      </View>
    );
  }
}

export default LoginScreen;

const styles = StyleSheet.create({
  container: {
    height: "80%",
    alignItems: "center",
    justifyContent: "center"
  },
  formWrapper: {
    width: "80%"
  },
  formRow: {

  },
  textInput: {
    borderRadius: 4, 
    backgroundColor: "#ddd",
    height: 40,
    paddingHorizontal: 10,
    marginBottom: 10,
    color: "#333"
  },
  loading: {
    height: "80%",
    flex: 1,
    justifyContent: "center",
    alignItems: "center"
  },
  welcomeText: {
    textAlign: "center",
    marginBottom: 20,
    fontSize: 24,
    fontWeight: "bold"
  },
  signInBtn: {
    backgroundColor: "#0095f6",
    borderRadius: 4, 
    width: "80%",
    paddingVertical: 10,
    marginTop: 20
  },
  signInText: {
    textAlign: "center",
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold"
  },
  disabledBtn: {
    opacity: 0.3,
    backgroundColor: "#0095f6",
    borderRadius: 4, 
    width: "80%",
    paddingVertical: 10,
    marginTop: 20
  }

});

