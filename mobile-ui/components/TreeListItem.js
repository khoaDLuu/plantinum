import React from 'react';
import { Text, View, Image, StyleSheet, TouchableOpacity } from 'react-native';

export default class TreeListItem extends React.Component {
    
    render() {
    const { tree, onPress } = this.props;
    return (
            <TouchableOpacity activeOpacity={0.7} 
                onPress={onPress}
            > 
                <View style={styles.container}>
                    <Image style={styles.treeImage} source={{ uri: tree.url }} />
                    <Text style={styles.name}>Hi im { tree.name }</Text>
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
        
        shadowColor: '#000',
        shadowOpacity: 0.5,
        shadowOffset: { width: 0, height: 0 },
    },
    treeImage: {
        width: 125,
        height: 125,
        marginLeft: -10,
    },
    name: {
        fontSize: 24,
        marginTop: 32,
        fontFamily: "Gothic",
        color: "#707070",
        
    },

});