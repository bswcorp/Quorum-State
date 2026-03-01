import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Image source={{uri: 'https://raw.githubusercontent.com'}} style={styles.logo} />
      <Text style={styles.title}>QUORUM-STATE MOBILE</Text>
      <Text style={styles.status}>h2k Bridge: ACTIVE</Text>
      <Text style={styles.balance}>5,000,000 $QSTATE</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000428', alignItems: 'center', justifyContent: 'center' },
  logo: { width: 150, height: 150, marginBottom: 20 },
  title: { color: '#00D2FF', fontSize: 24, fontWeight: 'bold' },
  status: { color: '#00FF00', marginTop: 10 },
  balance: { color: 'white', fontSize: 30, marginTop: 20 }
});
