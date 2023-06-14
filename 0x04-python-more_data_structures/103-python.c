#include <python3.4m/Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic information about a Python list.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;

size = PyObject_Length(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, item->ob_type->tp_name);
if (PyObject_IsInstance(item, (PyObject *)&PyBytes_Type))
print_python_bytes(item);
}
}

/**
 * print_python_bytes - Prints basic information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");

if (!PyObject_IsInstance(p, (PyObject *)&PyBytes_Type))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyObject_Length(p);
str = PyBytes_AsString(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", str);

printf("  first %zd bytes:", size > 10 ? 10 : size);
for (i = 0; i < size && i < 10; i++)
printf(" %02hhx", str[i]);
printf("\n");
}

