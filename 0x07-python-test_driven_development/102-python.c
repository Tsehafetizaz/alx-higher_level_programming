#include <Python.h>
#include <object.h>
#include <unicodeobject.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		printf("[ERROR] Invalid String Object\n");
		return;
	}

	printf("[.] string object info\n");

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	Py_ssize_t length = PyUnicode_GET_LENGTH(p);

	printf("  length: %zd\n", length);

	PyObject *str_repr = PyUnicode_AsUTF8String(p);

	if (str_repr != NULL)
	{
		char *string = PyBytes_AsString(str_repr);

		if (string != NULL)
		{
			printf("  value: %s\n", string);
		}
		else
		{
			printf("  [ERROR] Failed to convert string to UTF-8\n");
		}
		Py_DECREF(str_repr);
	}
	else
	{
		printf("  [ERROR] Failed to convert string to UTF-8\n");
	}
}
