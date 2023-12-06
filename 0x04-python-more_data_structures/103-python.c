#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{

	if (!PyList_Check(p))
	{
		printf("Invalid List Object\n");
		return;
	}


	Py_ssize_t size = PyList_GET_SIZE(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;


	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);


	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %zd: %s\n", i, item->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}


	Py_ssize_t size = PyBytes_Size(p);
	char *c_string = PyBytes_AsString(p);


	printf("[.] bytes object info\n");
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", c_string);


	printf("  first 10 bytes: ");
	for (int i = 0; (i < size) && (i < 10); i++)
	{
		printf("%02x ", (unsigned char)c_string[i]);
	}
	printf("\n");
}
