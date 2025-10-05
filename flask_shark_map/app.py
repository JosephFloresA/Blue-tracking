from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import random

app = Flask(__name__)

# Shark data from your notebook
datos_tiburones = {'color_punto': ['Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Magenta',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Verde',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris',
  'Gris'],
 'longitud': [-73.51,
  -65.75,
  -66.04,
  -66.14,
  -65.88,
  -66.87,
  -67.44,
  -67.17,
  -66.87,
  -67.74,
  -67.01,
  -67.57,
  -67.14,
  -67.8,
  -67.34,
  -72.02,
  -67.57,
  -73.18,
  -67.7,
  -73.41,
  -73.75,
  -65.61,
  -76.43,
  -75.34,
  -64.88,
  -64.48,
  -78.26,
  -76.97,
  -77.7,
  -63.29,
  -77.26,
  -77.23,
  -77.4,
  -63.22,
  -63.49,
  -63.39,
  -77.99,
  -78.09,
  -62.86,
  -63.12,
  -63.16,
  -64.48,
  -66.48,
  -64.32,
  -66.58,
  -72.22,
  -62.76,
  -65.51,
  -65.35,
  -69.46,
  -65.95,
  -65.08,
  -67.6,
  -64.42,
  -64.88,
  -66.31,
  -64.72,
  -65.31,
  -59.14,
  -60.63,
  -57.02,
  -59.37,
  -52.87,
  -57.91,
  -58.28,
  -57.31,
  -65.38,
  -66.08,
  -65.78,
  -61.1,
  -59.51,
  -61.43,
  -61.63,
  -63.56,
  -62.23,
  -63.09,
  -61.8,
  -62.89,
  -63.02,
  -62.79,
  -62.92,
  -62.59,
  -62.29,
  -63.52,
  -63.06,
  -63.29,
  -63.65,
  -63.72,
  -63.02,
  -63.39,
  -64.48,
  -64.62,
  -64.82,
  -64.45,
  -64.65,
  -62.96,
  -64.45,
  -62.49,
  -63.16,
  -62.96,
  -63.42,
  -64.92,
  -63.09,
  -64.15,
  -64.65,
  -64.39,
  -63.82,
  -63.32,
  -63.59,
  -63.65,
  -64.42,
  -64.02,
  -63.85,
  -64.25,
  -63.75,
  -63.99,
  -63.99,
  -77.03,
  -66.38,
  -71.09,
  -66.41,
  -68.14,
  -70.79,
  -66.28,
  -66.11,
  -68.67,
  -70.76,
  -72.65,
  -66.91,
  -68.27,
  -68.47,
  -66.48,
  -68.8,
  -72.55,
  -66.94,
  -66.11,
  -75.24,
  -66.34,
  -79.22,
  -77.56,
  -63.85,
  -63.59,
  -63.72,
  -78.29,
  -63.39,
  -63.59,
  -77.76,
  -78.06,
  -63.46,
  -63.69,
  -76.97,
  -77.16,
  -79.52,
  -79.39,
  -77.6,
  -79.12,
  -77.23,
  -79.19,
  -63.12,
  -63.49,
  -77.6,
  -63.32,
  -79.16,
  -62.99,
  -63.32,
  -62.92,
  -63.19,
  -62.79,
  -71.16,
  -61.83,
  -72.02,
  -66.71,
  -68.47,
  -71.19,
  -61.8,
  -63.99,
  -66.78,
  -61.86,
  -62.09,
  -62.56,
  -63.65,
  -62.26,
  -63.19,
  -66.64,
  -68.53,
  -62.69,
  -63.32,
  -63.65,
  -63.99,
  -61.3,
  -61.63,
  -62.16,
  -61.5,
  -63.39,
  -58.97,
  -62.82,
  -63.12,
  -62.63,
  -62.89,
  -63.06,
  -57.81,
  -75.54,
  -62.86,
  -63.12,
  -57.95,
  -62.76,
  -63.02,
  -62.96,
  -63.29,
  -62.96,
  -63.22,
  -51.8,
  -50.05,
  -53.6,
  -49.32,
  -56.02,
  -55.89,
  -64.05,
  -49.38,
  -58.51,
  -50.11,
  -56.85,
  -58.68,
  -56.58,
  -49.02,
  -76.04,
  -62.33,
  -65.08,
  -66.68,
  -66.31,
  -64.98,
  -64.95,
  -64.62],
 'latitud': [25.8,
  25.97,
  25.94,
  26.19,
  26.22,
  26.31,
  26.28,
  26.22,
  26.42,
  26.39,
  26.47,
  26.5,
  26.53,
  26.56,
  26.64,
  26.42,
  26.76,
  26.76,
  26.76,
  26.84,
  26.47,
  27.38,
  27.75,
  27.46,
  28.14,
  28.51,
  29.61,
  29.78,
  29.78,
  30.23,
  30.43,
  30.09,
  30.46,
  30.54,
  30.66,
  30.88,
  30.91,
  31.14,
  33.65,
  33.73,
  33.93,
  34.33,
  34.33,
  34.44,
  34.53,
  34.3,
  34.16,
  34.55,
  34.55,
  34.3,
  34.47,
  34.44,
  34.5,
  34.69,
  34.61,
  34.67,
  34.75,
  34.78,
  34.78,
  34.92,
  35.68,
  37.75,
  37.29,
  38.54,
  38.85,
  38.9,
  40.82,
  40.97,
  41.11,
  37.77,
  38.06,
  38.28,
  38.54,
  38.14,
  38.96,
  39.24,
  39.05,
  39.02,
  39.36,
  39.53,
  39.58,
  39.58,
  39.38,
  39.55,
  39.69,
  39.53,
  39.69,
  39.78,
  39.81,
  39.89,
  40.03,
  40.2,
  40.12,
  40.29,
  40.32,
  40.34,
  40.46,
  40.32,
  40.43,
  40.54,
  40.6,
  40.74,
  40.74,
  40.8,
  40.66,
  40.85,
  40.82,
  40.85,
  40.91,
  41.14,
  41.08,
  41.05,
  41.22,
  41.28,
  41.28,
  41.31,
  41.39,
  25.94,
  26.11,
  26.16,
  26.25,
  26.25,
  26.05,
  26.28,
  26.36,
  26.31,
  26.33,
  26.42,
  26.56,
  26.53,
  26.56,
  26.56,
  26.53,
  26.64,
  26.76,
  26.84,
  27.07,
  27.01,
  28.03,
  28.2,
  28.99,
  29.13,
  29.27,
  29.19,
  29.27,
  29.44,
  28.73,
  29.89,
  29.98,
  29.98,
  30.57,
  30.68,
  30.57,
  30.77,
  30.68,
  30.8,
  30.85,
  31.02,
  30.97,
  30.99,
  30.97,
  31.16,
  31.25,
  32.01,
  32.01,
  32.86,
  32.92,
  33.11,
  33.93,
  34.07,
  34.02,
  34.33,
  34.36,
  34.21,
  34.36,
  34.53,
  34.55,
  34.58,
  34.61,
  34.61,
  34.53,
  34.64,
  34.58,
  34.67,
  34.58,
  34.75,
  34.75,
  34.72,
  34.69,
  34.67,
  34.72,
  34.89,
  34.95,
  34.92,
  35.01,
  34.98,
  34.92,
  35.03,
  35.15,
  35.15,
  34.92,
  35.29,
  35.29,
  35.32,
  35.15,
  35.57,
  35.6,
  36.28,
  36.33,
  36.7,
  36.79,
  37.32,
  37.41,
  37.49,
  38.2,
  38.08,
  38.28,
  38.25,
  38.42,
  38.37,
  38.4,
  38.48,
  38.56,
  38.59,
  38.31,
  39.41,
  39.78,
  40.43,
  40.46,
  40.63,
  40.8,
  40.99,
  41.11]}

import joblib
import os

# Try to load the chlorophyll data with better error handling
try:
    pkl_path = 'C:\\Users\\josep\\OneDrive\\Escritorio\\space app\\data_map\\data_clorofile.pkl'
    if os.path.exists(pkl_path):
        data_clorofile = joblib.load(pkl_path)
        print(f"Successfully loaded chlorophyll data. Available months: {list(data_clorofile.keys())}")
    else:
        print(f"Warning: Chlorophyll data file not found at {pkl_path}")
        data_clorofile = {}
except Exception as e:
    print(f"Error loading chlorophyll data: {e}")
    data_clorofile = {}


# try to load humedad data
try:
    pkl_path_humedad = 'C:\\Users\\josep\\OneDrive\\Escritorio\\space app\\data_map\\data_hum.pkl'
    if os.path.exists(pkl_path_humedad):
        data_humedad = joblib.load(pkl_path_humedad)
        print(f"Successfully loaded humidity data. Available months: {list(data_humedad.keys())}")
    else:
        print(f"Warning: Humidity data file not found at {pkl_path_humedad}")
        data_humedad = {}
except Exception as e:
    print(f"Error loading humidity data: {e}")
    data_humedad = {}

# Generate dummy temperature data

def generate_dummy_environmental_data():
    """Generate realistic temperature and pressure data based on seasonal and geographic patterns"""
    
    # Bounds: X (-84.6° to -45°), Y (43° to 23°)
    lon_min, lon_max = -84.6, -45.0
    lat_min, lat_max = 23.0, 43.0
    
    # Generate data for 12 months (2013)
    months = [f"2013{str(i).zfill(2)}" for i in range(1, 13)]
    
    temperature_data = {}
    pressure_data = {}
    
    for i, month in enumerate(months):
        month_num = i + 1  # 1-12
        
        # Generate realistic number of points (more in extreme weather months)
        if month_num in [1, 2, 7, 8]:  # Winter and summer peaks
            num_temp_points = random.randint(2800, 3500)
            num_press_points = random.randint(2200, 2800)
        else:
            num_temp_points = random.randint(1500, 2500)
            num_press_points = random.randint(1200, 2000)
        
        # Generate coordinates
        temp_lons = np.random.uniform(lon_min, lon_max, num_temp_points)
        temp_lats = np.random.uniform(lat_min, lat_max, num_temp_points)
        press_lons = np.random.uniform(lon_min, lon_max, num_press_points)
        press_lats = np.random.uniform(lat_min, lat_max, num_press_points)
        
        # REALISTIC TEMPERATURE CALCULATION
        # Seasonal factor: cosine wave with minimum in January, maximum in July
        seasonal_factor = np.cos(2 * np.pi * (month_num - 7) / 12)  # -1 to 1
        
        # Calculate temperature for each point
        temperatures = []
        for lat in temp_lats:
            # Base temperature decreases with latitude (north colder)
            lat_effect = 35 - (lat - lat_min) * 0.8  # 35°C at south, ~19°C at north
            
            # Seasonal variation: ±10°C swing
            seasonal_temp = lat_effect + seasonal_factor * 10
            
            # Add some random variation ±3°C
            final_temp = seasonal_temp + np.random.normal(0, 3)
            
            # Keep within reasonable bounds (0°C to 45°C)
            final_temp = max(0, min(45, final_temp))
            temperatures.append(final_temp)
        
        # REALISTIC PRESSURE CALCULATION - LARGE DISPERSED PATCH/CLUSTER GENERATION
        # Generate 4-6 pressure systems (fewer but larger patches) per month
        num_systems = random.randint(4, 6)
        
        press_lons_clustered = []
        press_lats_clustered = []
        pressures = []
        
        for system in range(num_systems):
            # Define center of each pressure system
            center_lon = np.random.uniform(lon_min + 1, lon_max - 1)  # Allow closer to edges
            center_lat = np.random.uniform(lat_min + 1, lat_max - 1)
            
            # System characteristics - MUCH LARGER AND MORE DISPERSED SYSTEMS
            system_strength = np.random.uniform(0.8, 1.4)  # Stronger intensity range
            system_size = np.random.uniform(10, 25)  # EVEN LARGER radius (10-25 degrees)
            
            # High pressure in winter, lower in summer, modified by system strength
            base_pressure = (1013 - seasonal_factor * 8) * system_strength
            
            # Number of points in this system (cluster) - MUCH FEWER POINTS for minimal accumulation
            points_in_system = random.randint(80, 200)  # Very low density for minimal clustering
            
            for _ in range(points_in_system):
                # Generate points with MAXIMUM spread for minimal clustering
                # Use multiple distribution methods with heavy bias toward dispersion
                spread_factor = system_size / 1.0  # Maximum spread (was /1.5)
                
                # Heavily favor uniform distribution for maximum dispersion
                if np.random.random() < 0.3:  # Only 30% normal distribution
                    point_lon = np.random.normal(center_lon, spread_factor)
                    point_lat = np.random.normal(center_lat, spread_factor)
                else:  # 70% uniform distribution for maximum dispersion
                    angle = np.random.uniform(0, 2 * np.pi)
                    radius = np.random.uniform(system_size * 0.3, system_size)  # Avoid center concentration
                    point_lon = center_lon + radius * np.cos(angle)
                    point_lat = center_lat + radius * np.sin(angle)
                
                # Keep within bounds
                point_lon = max(lon_min, min(lon_max, point_lon))
                point_lat = max(lat_min, min(lat_max, point_lat))
                
                # Distance from center affects pressure intensity - MINIMAL GRADIENT for less accumulation
                distance_from_center = np.sqrt((point_lon - center_lon)**2 + (point_lat - center_lat)**2)
                distance_factor = max(0.7, 1 - (distance_from_center / system_size)**0.3)  # Almost flat gradient
                
                # Calculate pressure for this point
                system_pressure = base_pressure * distance_factor
                
                # Latitude effect (slight decrease with latitude)
                lat_pressure = system_pressure - (point_lat - lat_min) * 0.2
                
                # Add maximum random variation for highly dispersed appearance
                weather_variation = np.random.normal(0, 12)  # Maximum variation for minimal clustering
                
                final_pressure = lat_pressure + weather_variation
                
                # Keep within realistic bounds
                final_pressure = max(980, min(1040, final_pressure))
                
                press_lons_clustered.append(point_lon)
                press_lats_clustered.append(point_lat)
                pressures.append(final_pressure)
        
        # ADD SCATTERED BACKGROUND POINTS (variance in empty zones)
        background_points = random.randint(800, 1200)  # Many background points to compensate for sparse clusters
        
        for _ in range(background_points):
            # Generate completely random points
            bg_lon = np.random.uniform(lon_min, lon_max)
            bg_lat = np.random.uniform(lat_min, lat_max)
            
            # Lower pressure for background (transitional zones)
            bg_base_pressure = 1000 + seasonal_factor * 5  # Lower baseline
            
            # Add significant variation for background "noise"
            bg_variation = np.random.normal(0, 12)  # Higher variation for scattered points
            
            bg_pressure = bg_base_pressure + bg_variation
            
            # Keep within bounds
            bg_pressure = max(985, min(1025, bg_pressure))  # Slightly narrower range
            
            press_lons_clustered.append(bg_lon)
            press_lats_clustered.append(bg_lat)
            pressures.append(bg_pressure)
        
        # Convert to numpy arrays
        press_lons = np.array(press_lons_clustered)
        press_lats = np.array(press_lats_clustered)
        pressures = np.array(pressures)
        
        # Filter for "high condition" points only (representing high pressure systems)
        # Temperature: Keep points above seasonal average
        temp_threshold = np.mean(temperatures) + np.std(temperatures) * 0.3
        high_temp_indices = [i for i, t in enumerate(temperatures) if t > temp_threshold]
        
        # Pressure: Keep broader range to show both clusters and scattered points
        press_threshold = np.mean(pressures) - np.std(pressures) * 0.1  # Very permissive to show most data
        high_press_indices = [i for i, p in enumerate(pressures) if p > press_threshold]
        
        # Store filtered high-condition points
        temperature_data[month] = {
            'lons': temp_lons[high_temp_indices],
            'lats': temp_lats[high_temp_indices],
            'values': np.array(temperatures)[high_temp_indices]
        }
        
        pressure_data[month] = {
            'lons': press_lons[high_press_indices],
            'lats': press_lats[high_press_indices],
            'values': pressures[high_press_indices]
        }
        
        # Debug info for pressure systems
        print(f"Month {month}: Generated {num_systems} large pressure systems + {background_points} scattered points = {len(high_press_indices)} total points")
    
    return temperature_data, pressure_data

def generate_realistic_humidity_data():
    """Generate realistic humidity data based on seasonal and geographic patterns"""
    
    # Bounds: X (-84.6° to -45°), Y (43° to 23°)
    lon_min, lon_max = -84.6, -45.0
    lat_min, lat_max = 23.0, 43.0
    
    months = [f"2013{str(i).zfill(2)}" for i in range(1, 13)]
    humidity_data = {}
    
    for i, month in enumerate(months):
        month_num = i + 1  # 1-12
        
        # More humidity points in summer (high evaporation) and coastal areas
        if month_num in [6, 7, 8, 9]:  # Summer months
            num_points = random.randint(2000, 3000)
        else:
            num_points = random.randint(1000, 2000)
        
        # Generate coordinates with bias toward coastal areas (edges)
        hum_lons = []
        hum_lats = []
        
        for _ in range(num_points):
            # 60% chance for coastal areas, 40% for inland
            if np.random.random() < 0.6:
                # Coastal bias - near edges of domain
                if np.random.random() < 0.5:
                    # Eastern or western coast
                    lon = np.random.choice([
                        np.random.uniform(lon_min, lon_min + 5),  # Western edge
                        np.random.uniform(lon_max - 5, lon_max)   # Eastern edge
                    ])
                    lat = np.random.uniform(lat_min, lat_max)
                else:
                    # Northern or southern coast
                    lat = np.random.choice([
                        np.random.uniform(lat_max - 3, lat_max),  # Northern edge
                        np.random.uniform(lat_min, lat_min + 3)   # Southern edge
                    ])
                    lon = np.random.uniform(lon_min, lon_max)
            else:
                # Inland areas
                lon = np.random.uniform(lon_min + 5, lon_max - 5)
                lat = np.random.uniform(lat_min + 3, lat_max - 3)
            
            hum_lons.append(lon)
            hum_lats.append(lat)
        
        # Calculate realistic humidity values
        # Seasonal factor: higher in summer, lower in winter
        seasonal_factor = np.sin(2 * np.pi * (month_num - 3) / 12)  # Peak in summer
        
        humidity_values = []
        for j, (lon, lat) in enumerate(zip(hum_lons, hum_lats)):
            # Base humidity: higher near coasts and in south
            coast_distance = min(
                abs(lon - lon_min), abs(lon - lon_max),  # Distance to E/W coast
                abs(lat - lat_min), abs(lat - lat_max)   # Distance to N/S coast
            )
            
            # Higher humidity near coasts
            coast_effect = max(0, 5 - coast_distance) * 3  # 0-15% boost near coasts
            
            # Latitude effect: more humid in south (subtropical)
            lat_effect = (lat_max - lat) * 1.5  # 0-30% based on latitude
            
            # Seasonal effect: ±20% swing
            seasonal_humidity = 45 + seasonal_factor * 20 + lat_effect + coast_effect
            
            # Add random variation
            final_humidity = seasonal_humidity + np.random.normal(0, 8)
            
            # Keep within bounds (20-95%)
            final_humidity = max(20, min(95, final_humidity))
            humidity_values.append(final_humidity)
        
        # Filter for high humidity conditions only (>70%)
        high_humidity_threshold = 70
        high_hum_indices = [i for i, h in enumerate(humidity_values) if h > high_humidity_threshold]
        
        if high_hum_indices:
            humidity_data[month] = (
                np.array(hum_lons)[high_hum_indices],
                np.array(hum_lats)[high_hum_indices]
            )
    
    return humidity_data

# Generate all realistic environmental data
data_temperatura, data_presion = generate_dummy_environmental_data()
data_humedad_realistic = generate_realistic_humidity_data()

# Override original humidity data with realistic data if no real data exists
if not data_humedad:  # Only if no real humidity data was loaded
    data_humedad = data_humedad_realistic
    print(f"Generated realistic humidity data for months: {list(data_humedad.keys())}")

print(f"Generated temperature data for months: {list(data_temperatura.keys())}")
print(f"Generated pressure data for months: {list(data_presion.keys())}")
print(f"Total humidity months available: {len(data_humedad)}")



# Create DataFrame
df = pd.DataFrame(datos_tiburones)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/shark_data')
def get_shark_data():
    """Return shark data as JSON for the map"""
    # Convert DataFrame to list of dictionaries for JSON serialization
    data = df.to_dict('records')
    return jsonify(data)

@app.route('/api/chlorophyll/available')
def get_available_months():
    """Return list of available months"""
    return jsonify({
        'available_months': list(data_clorofile.keys()),
        'total_months': len(data_clorofile)
    })

@app.route('/api/chlorophyll/<mes>')
def get_chlorophyll_data(mes):
    """Return chlorophyll border data for a given month"""
    try:
        print(f"Requesting chlorophyll data for month: {mes}")
        print(f"Available months in data: {list(data_clorofile.keys())}")
        
        if mes in data_clorofile:
            lon_border, lat_border = data_clorofile[mes]
            # Convert numpy float32 to regular Python float for JSON serialization
            border_data = [{'longitude': float(lon), 'latitude': float(lat)} for lon, lat in zip(lon_border, lat_border)]
            print(f"Found {len(border_data)} data points for month {mes}")
            return jsonify(border_data)
        else:
            print(f"Month {mes} not found in chlorophyll data")
            return jsonify({'error': f'No data found for month {mes}', 'available_months': list(data_clorofile.keys())})
    except Exception as e:
        print(f"Error in get_chlorophyll_data: {e}")
        return jsonify({'error': str(e)}), 500



@app.route('/api/humidity/available')
def get_available_humidity_months():
    """Return list of available months for humidity data"""
    return jsonify({
        'available_months': list(data_humedad.keys()),
        'total_months': len(data_humedad)
    })


@app.route('/api/humidity/<mes>')
def get_humidity_data(mes):
    """Return humidity border data for a given month"""
    try:
        print(f"Requesting humidity data for month: {mes}")
        print(f"Available months in humidity data: {list(data_humedad.keys())}")
        
        if mes in data_humedad:
            lon_border, lat_border = data_humedad[mes]
            # Convert numpy float32 to regular Python float for JSON serialization
            border_data = [{'longitude': float(lon), 'latitude': float(lat)} for lon, lat in zip(lon_border, lat_border)]
            print(f"Found {len(border_data)} data points for month {mes}")
            return jsonify(border_data)
        else:
            print(f"Month {mes} not found in humidity data")
            return jsonify({'error': f'No data found for month {mes}', 'available_months': list(data_humedad.keys())})
    except Exception as e:
        print(f"Error in get_humidity_data: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/temperature/available')
def get_available_temperature_months():
    """Return list of available months for temperature data"""
    return jsonify({
        'available_months': list(data_temperatura.keys()),
        'total_months': len(data_temperatura)
    })


@app.route('/api/temperature/<mes>')
def get_temperature_data(mes):
    """Return temperature data for a given month"""
    try:
        print(f"Requesting temperature data for month: {mes}")
        
        if mes in data_temperatura:
            temp_data = data_temperatura[mes]
            # Convert to list of dictionaries for JSON
            result = []
            for i in range(len(temp_data['lons'])):
                result.append({
                    'longitude': float(temp_data['lons'][i]),
                    'latitude': float(temp_data['lats'][i]),
                    'temperature': float(temp_data['values'][i])
                })
            print(f"Found {len(result)} temperature points for month {mes}")
            return jsonify(result)
        else:
            print(f"Month {mes} not found in temperature data")
            return jsonify({'error': f'No data found for month {mes}', 'available_months': list(data_temperatura.keys())})
    except Exception as e:
        print(f"Error in get_temperature_data: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/pressure/available')
def get_available_pressure_months():
    """Return list of available months for pressure data"""
    return jsonify({
        'available_months': list(data_presion.keys()),
        'total_months': len(data_presion)
    })


@app.route('/api/pressure/<mes>')
def get_pressure_data(mes):
    """Return pressure data for a given month"""
    try:
        print(f"Requesting pressure data for month: {mes}")
        
        if mes in data_presion:
            press_data = data_presion[mes]
            # Convert to list of dictionaries for JSON
            result = []
            for i in range(len(press_data['lons'])):
                result.append({
                    'longitude': float(press_data['lons'][i]),
                    'latitude': float(press_data['lats'][i]),
                    'pressure': float(press_data['values'][i])
                })
            print(f"Found {len(result)} pressure points for month {mes}")
            return jsonify(result)
        else:
            print(f"Month {mes} not found in pressure data")
            return jsonify({'error': f'No data found for month {mes}', 'available_months': list(data_presion.keys())})
    except Exception as e:
        print(f"Error in get_pressure_data: {e}")
        return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)