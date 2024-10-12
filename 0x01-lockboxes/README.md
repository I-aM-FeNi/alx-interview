### `README.md`

# Lockboxes Project

This project contains a Python function that determines if all boxes in a list can be opened. Each box may contain keys to other boxes, and the goal is to check if all boxes can be unlocked starting from the first box.

## Description

The `canUnlockAll` function takes a list of lists as input, where each sublist represents a box and contains keys to other boxes. The function returns `True` if all boxes can be opened, otherwise it returns `False`.

## Requirements

- Python 3.4.3 or later
- PEP 8 style guidelines

## Files

- `0-lockboxes.py`: Contains the `canUnlockAll` function.
- `main_0.py`: Script to test the `canUnlockAll` function with various test cases.
- `README.md`: Project documentation.

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/alx-interview.git
    cd alx-interview/0x01-lockboxes
    ```

2. **Make the scripts executable**:
    ```sh
    chmod +x 0-lockboxes.py main_0.py
    ```

3. **Run the test script**:
    ```sh
    ./main_0.py
    ```

## Example

Here is an example of how to use the `canUnlockAll` function:

```python
#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
```

## Function Documentation

### `canUnlockAll`

```python
def canUnlockAll(boxes):
    """
    Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    Args:
        boxes (list of lists): List of boxes with keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation

1. **Project Title and Description**: Provides a brief overview of the project.
2. **Requirements**: Lists the requirements for running the project.
3. **Files**: Describes the files included in the project.
4. **Usage**: Provides instructions on how to clone the repository, make the scripts executable, and run the test script.
5. **Example**: Shows an example of how to use the `canUnlockAll` function.
6. **Function Documentation**: Provides detailed documentation for the `canUnlockAll` function.
7. **License**: Mentions the license under which the project is distributed.
