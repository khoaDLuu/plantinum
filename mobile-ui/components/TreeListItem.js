import React from 'react';
import { Text, View, Image, StyleSheet, TouchableOpacity } from 'react-native';
import alert from '../assets/alert.png';

export default class TreeListItem extends React.Component {
    
    render() {
    const { tree, onPress } = this.props;
    const { state, img_url } = tree.latest_data;
    return (
            <TouchableOpacity activeOpacity={0.7} 
                onPress={onPress}
            > 
                <View style={styles.container}>
                    <Image style={styles.treeImage} source={{ uri: img_url }} />
                    <Text style={styles.name}>{ tree.name }</Text>
                    { state !== "good" && <Image source={alert} style={styles.notification}/>}
                </View>
            </TouchableOpacity>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        display: 'flex',
        flexDirection: 'row',
        padding: 16,
        borderRadius: 12,
        marginBottom: 16,
        backgroundColor: '#FFF',
        position: "relative",
        shadowColor: '#000',
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 0 },
    },
    treeImage: {
        width: 125,
        height: 125,
        marginLeft: -10,
        borderRadius: 8,
    },
    name: {
        fontSize: 24,
        marginTop: 32,
        marginLeft: 50,
        fontFamily: "Gothic",
        color: "#707070",
        
    },
    notification: {
        width: 25,
        height: 25,
        position: "absolute",
        top: 5,
        right: 15,
    }
});