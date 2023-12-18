#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>

/**
 * print_python_list - Print basic info about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - Print basic info about Python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *string_representation;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string_representation = PyBytes_AsString(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string_representation);

	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	for (i = 0; i < size && i < 10; i++)
	{
		printf(" %02x", string_representation[i] & 0xff);
	}
	printf("\n");
}

/**
 * print_python_float - Print basic info about Python float objects
 * @p: PyObject float object
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AS_DOUBLE(p);
	printf("  value: %lf\n", value);
}
