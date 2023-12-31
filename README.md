# Gravity Ball Display with GC9A01 and BMI160

This Python code makes use of the `GC9A01` display and `BMI160` gravity sensor to simulate a ball moving across the display based on the gravitational pull (acceleration) sensed by the BMI160.

## 📌 Requirements

- CircuitPython-compatible board.
- `GC9A01` round display module.
- `BMI160` 3-axis accelerometer.
- `geometry_helper` module (for determining the ball's position within the display's circular confines).

## 🔌 Setup

1. **Connect the Display and Sensor Pins**:
    - **Display Configuration**:
      ```
      TFT_RST -> GP7   (ORANGE)
      TFT_DC  -> GP6   (GREEN)
      TFT_CS  -> GP5   (BLUE)
      TFT_SCK -> GP2   (WHITE)
      TFT_MOSI-> GP3   (YELLOW)
      TFT_BL  -> GP4   (PURPLE)
      ```
    - **Gravity Sensor Configuration**:
      ```
      RED    -> 3.3v
      BLACK  -> GND
      YELLOW -> SCL (GP27)
      WHITE  -> SDA (GP26)
      ```

2. Transfer the code to your CircuitPython device.

3. Reset the device.

## 🔄 Operation

When powered, the program will:

1. Initialize the display and draw a static background with a ball in the center.
2. Configure the BMI160 accelerometer.
3. Continuously fetch the x and y acceleration from the BMI160 sensor.
4. Translate this acceleration into the speed in which the ball should move on the display.
5. Update the ball's position using geometric calculations to ensure the ball doesn't exit the round confines of the display.
6. Render the ball at its new position on the display, thus visually representing the acceleration sensed by the BMI160 in real-time.

## 📝 Note

There's commented-out code related to NeoPixels. If you'd like to integrate lighting effects with the motion of the ball, uncomment and adapt that code.