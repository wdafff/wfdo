module github.com/uptrace/go-clickhouse/example/basic

go 1.18

replace github.com/uptrace/go-clickhouse => ../..

replace github.com/uptrace/go-clickhouse/chdebug => ../../chdebug

require (
<<<<<<< HEAD
	github.com/uptrace/go-clickhouse v0.3.0
	github.com/uptrace/go-clickhouse/chdebug v0.3.0
=======
	github.com/uptrace/go-clickhouse v0.3.1
	github.com/uptrace/go-clickhouse/chdebug v0.3.1
>>>>>>> e4f2453f975d3b251949d795bb2dcf4aa58e12fa
)

require (
	github.com/codemodus/kace v0.5.1 // indirect
	github.com/fatih/color v1.14.1 // indirect
	github.com/jinzhu/inflection v1.0.0 // indirect
	github.com/mattn/go-colorable v0.1.13 // indirect
	github.com/mattn/go-isatty v0.0.17 // indirect
	github.com/pierrec/lz4/v4 v4.1.17 // indirect
<<<<<<< HEAD
	go.opentelemetry.io/otel v1.11.2 // indirect
	go.opentelemetry.io/otel/trace v1.11.2 // indirect
	golang.org/x/exp v0.0.0-20230118134722-a68e582fa157 // indirect
	golang.org/x/sys v0.4.0 // indirect
=======
	go.opentelemetry.io/otel v1.13.0 // indirect
	go.opentelemetry.io/otel/trace v1.13.0 // indirect
	golang.org/x/exp v0.0.0-20230213192124-5e25df0256eb // indirect
	golang.org/x/sys v0.5.0 // indirect
>>>>>>> e4f2453f975d3b251949d795bb2dcf4aa58e12fa
)
