import React from 'react';
import { StyleSheet, FlatList, ActivityIndicator, View } from 'react-native';
import TreeListItem from '../components/TreeListItem';
import axios from 'axios';

export default class Trees extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      trees: [],
      dataLoaded: false
    };
  }
  async componentDidMount() {
    const data = await axios.get('http://4d753b72.ngrok.io/trees');
    this.setState({ 
      trees: data.data,
      dataLoaded: true
    });
  }
  render() {
    const { navigation } = this.props;
    const { trees } = this.state;
    return (
      <View>
        { this.state.dataLoaded ? 
          (<FlatList 
            data={trees}
            renderItem={({ item }) => 
            <TreeListItem tree={item}
              onPress={() => navigation.navigate('Home2', {
                treeName: item.name,
                imageUrl: item.url,
                temperature: item.temperature,
                humidity: item.humidity,
                moisture: item.moisture,
                lightIntensity: item.lightIntensity
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
    paddingTop: "50%"
  }
});
