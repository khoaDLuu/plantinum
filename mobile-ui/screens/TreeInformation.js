import React from 'react';
import { StyleSheet, Text, View, Image, ScrollView } from 'react-native';

import TreeInformationList from '../components/TreeInformationList';
export default class TreeInformation extends React.Component {
  // const {  }
  

  render() {
    const { imageUrl, treeName, temperature, humidity, moisture, lightIntensity } = this.props.route.params;
    return (
      <ScrollView>
        <View style={styles.container}>
          <View style={styles.contentContainer}>
            <Image style={{width: 128, height: 128, marginTop: 5}}  source={{ uri: imageUrl  }} />
            <Text style={styles.title}>{treeName}</Text>
            <View  style={styles.info}>
            <TreeInformationList 
              temperature={temperature}
              humidity={humidity}
              moisture={moisture}
              lightIntensity={lightIntensity}
            />
            </View>
          </View>
        </View>
      </ScrollView>

    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    // justifyContent: 'center',
    // paddingHorizontal: 16,
    backgroundColor: "#58B0AE",
    padding: 16
  },
  contentContainer: {
    flex: 1,
    alignItems: 'center',
    height: "100%",
    width: "100%",
    backgroundColor: "#FFF",
    borderRadius: 12,
    shadowColor: '#000',
    shadowOpacity: 0.5,
    shadowOffset: { width: 0, height: 0 },
  },
  title: { 
    fontFamily: "Gothic",
    fontSize: 40,
    color: "#707070",
    paddingTop: 5
  },

  info: {
    marginLeft: 0,
    marginTop: 25
  }
});
