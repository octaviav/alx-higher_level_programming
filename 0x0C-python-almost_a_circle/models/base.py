#!/usr/bin/python3

import json
import csv
from turtle import Turtle

class Base:
    """Base model.

    Represents the base class for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
            id (int): identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """Returns the deserialization of a JSON string.

        Args:
            json_string (str): A JSON string representation of a list of dictionaries.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    def _convert_to_int(dictionary):
        """Converts values in dictionary to int."""
        return {k: int(v) for k, v in dictionary.items()}

    def draw_shapes(t, shapes, color):
        """Draws shapes using the turtle module.

        Args:
            t (Turtle): Turtle object.
            shapes (list): list of shapes to draw.
            color (str): color to draw the shapes.
        """
        t.color(color)
        for shape in shapes:
            t.showturtle()
            t.up()
            t.goto(shape.x, shape.y)
            t.down()
            for _ in range(2):
                t.forward(shape.width)
                t.left(90)
                t.forward(shape.height)
                t.left(90)
            t.hideturtle()

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """Draws Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): list of Rectangle objects to draw.
            list_squares (list): list of Square objects to draw.
        """
        t = Turtle()
        t.screen.bgcolor("#b7312c")
        t.pensize(3)
        t.shape("turtle")

        cls.draw_shapes(t, list_rectangles, "#ffffff")
        cls.draw_shapes(t, list_squares, "#b5e3d8")

        t.screen.exitonclick()

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                fieldnames = cls._get_fieldnames()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = cls._get_fieldnames()
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [cls._convert_to_int(d) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def _get_fieldnames():
        """Returns field names for CSV serialization."""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]
 
