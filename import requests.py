import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(WeatherApp());
}

class WeatherApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Weather App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: WeatherHomePage(),
    );
  }
}

class WeatherHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final DateTime now = DateTime.now();
    final timeFormat = DateFormat.jm().format(now);

    return Scaffold(
      appBar: AppBar(
        title: Text('Weather App'),
      ),
      body: Container(
        decoration: BoxDecoration(
          gradient: getBackgroundGradient(now.hour),
        ),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Good $timeFormat',
                style: TextStyle(fontSize: 32),
              ),
              SizedBox(height: 20),
              Image.asset(
                getWeatherImage(now.hour),
                width: 120,
                height: 120,
              ),
              SizedBox(height: 20),
              Text(
                getWeatherCondition(now.hour),
                style: TextStyle(fontSize: 24),
              ),
            ],
          ),
        ),
      ),
    );
  }

  LinearGradient getBackgroundGradient(int hour) {
    if (hour >= 6 && hour < 18) {
      // Daytime gradient
      return LinearGradient(
        colors: [Colors.orange[200], Colors.blue[200]],
        begin: Alignment.topCenter,
        end: Alignment.bottomCenter,
      );
    } else {
      // Nighttime gradient
      return LinearGradient(
        colors: [Colors.indigo[900], Colors.black],
        begin: Alignment.topCenter,
        end: Alignment.bottomCenter,
      );
    }
  }

  String getWeatherImage(int hour) {
    if (hour >= 6 && hour < 18) {
      // Daytime weather
      return 'assets/sun.png';
    } else {
      // Nighttime weather
      return 'assets/moon.png';
    }
  }

  String getWeatherCondition(int hour) {
    if (hour >= 6 && hour < 18) {
      // Daytime weather condition
      return 'Sunny';
    } else {
      // Nighttime weather condition
      return 'Clear Sky';
    }
  }
}
