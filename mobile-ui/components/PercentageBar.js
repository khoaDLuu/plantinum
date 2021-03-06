import React from 'react';
import { Text, View, StyleSheet } from 'react-native';

export default class PercentageBar extends React.Component {

    render() {
        
        const { percent, unit, param } = this.props; 
        return (
            <View style={styles.bar}>
                <View style={{backgroundColor: "#7CB777", height: "100%", borderRadius: 7, width: percent + "%"}}>
                    <Text style={styles.percent}>{Math.ceil(param) + (unit ? unit : "")}</Text>
                </View>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    bar: {
        backgroundColor: "#FFF",
        width: 269,
        height: 20,
        borderRadius: 7,
        shadowColor: '#000',
        shadowOpacity: 0.2,
        shadowOffset: { width: 0, height: 2 },
    },
    percent: {
        textAlign: "center"
    }

    // percent: {
    //     backgroundColor: "#40B76C",
    //     height: "100%",
    //     borderRadius: 7,
    // }
});