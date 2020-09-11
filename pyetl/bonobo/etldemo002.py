import bonobo

def guess_email(**row):
    return {
            **row,
            'email': row['name'] + '@' + row['domain']
    }

graph = bonobo.Graph(
        bonobo.CsvReader('employees.csv'),
        bonobo.Filter(lambda *row: row['position'] != 'CEO'),
        # guess_email,
        bonobo.CsvWriter('employees.output.csv'),
)

if __name__ == "__main__":
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser):
        bonobo.run(graph)
