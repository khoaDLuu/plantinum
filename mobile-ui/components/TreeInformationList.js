import React from 'react';
import { Text, View, Image, StyleSheet, ScrollView } from 'react-native';

// import * as Progress from 'react-native-progress';
import temperatureIcon from '../assets/temperature.png';
import humidityIcon from '../assets/humidity.png';
import moistureIcon from '../assets/moisture.png';
import lightIntensityIcon from '../assets/light-intensity.png'
import PercentageBar from '../components/PercentageBar';

export default class TreeInformationList extends React.Component {
 
    render() {
        const { temperature, humidity, moisture, lightIntensity  } = this.props;
        return(
        <View>
                <View style={{marginBottom: 10}}>
                    <View style={styles.container}>
                        <Image source={temperatureIcon} style={styles.icon} />
                        <Text style={styles.title}>Temperature</Text>
                    </View>
                    <PercentageBar 
                        percent={temperature}
                    />
                </View>
                <View style={{marginBottom: 10}}>
                    <View style={styles.container}>
                        <Image source={humidityIcon} style={styles.icon} />
                        <Text style={styles.title}>Humidity</Text>
                    </View>
                    <PercentageBar 
                        percent={humidity}
                    />
                </View>
                <View style={{marginBottom: 10}}>
                    <View style={styles.container}>
                        <Image source={moistureIcon} style={styles.icon} />
                        <Text style={styles.title}>Moisture</Text>
                    </View>
                    <PercentageBar 
                        percent={moisture}
                    />
                </View>
                <View style={{marginBottom: 10}}>
                    <View style={styles.container}>
                        <Image source={lightIntensityIcon} style={styles.icon} />
                        <Text style={styles.title}>Light intensity</Text>
                    </View>
                    <PercentageBar 
                        percent={lightIntensity}
                    />
                </View>
        </View>);
    }

}

const styles = StyleSheet.create({
    container: {
        display: 'flex',
        flexDirection: "row",
        marginBottom: 10,

    },
    icon: {
        height: 50,
        width: 50,
        marginRight: 12
    }, 
    title: {
        color: "#707070",
        fontSize: 20
        
    }
});