import React from 'react';
import { StyleSheet, Text, View, Image, ScrollView } from 'react-native';

import TreeInformationList from '../components/TreeInformationList';
export default class TreeInformation extends React.Component {
  
  render() {
    const { img_url, name, temperature, humidity, moisture, light_intensity, state, time_recorded } = this.props.route.params.latest_data;
    const { type } = this.props.route.params;
    return (
      <ScrollView style={{height: "100%", backgroundColor: "#58B0AE"}}>
        <View style={styles.container}>
          <View style={styles.contentContainer}>
            <Image style={{width: 128, height: 128, marginTop: 5}}  source={{ uri: img_url }} />
            <Text style={styles.title}>{type}</Text>
            <Text style={styles.timeRecorded} >{`Last update in ${new Date(time_recorded).toLocaleString()}`}</Text>
            { state !== "good" && <Text style={styles.notification}>Your plant got problem please check</Text>}
            <View  style={styles.info}>
            <TreeInformationList 
              temperature={temperature}
              humidity={humidity}
              moisture={moisture}
              lightIntensity={light_intensity}
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
    justifyContent: 'center',
    alignItems: 'center',
    // paddingHorizontal: 16,
    // height: 800,
    backgroundColor: "#58B0AE",
    height: "100%",
    padding: 16
  },
  contentContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: "center",
    height: 700,
    width: "100%",
    backgroundColor: "#FFF",
    borderRadius: 12,
    shadowColor: '#000',
    shadowOpacity: 0.5,
    shadowOffset: { width: 0, height: 0 },
  },
  title: { 
    fontFamily: "Gothic",
    fontSize: 30,
    color: "#707070",
    paddingTop: 5
  },

  info: {
    marginLeft: 0,
    marginTop: 25
  },
  timeRecorded: {
  
  },
  notification: {
    color: "#E44242"
  }
});
