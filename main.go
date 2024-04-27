package main

import (
	"context"
	"fmt"
	"os"

	"dagger.io/dagger"
)

func main() {
	ctx := context.Background()

	client, err := dagger.Connect(ctx, dagger.WithLogOutput(os.Stderr))
	if err != nil {
		panic(err)
	}
	defer client.Close()

	mysqlPassword := "hogehoge"
	mysql := client.Container().
		From("mysql:8").
		WithExposedPort(3306).
		WithEnvVariable("MYSQL_ROOT_PASSWORD", mysqlPassword).
		AsService()

	django := client.Container().
		From("ghcr.io/wt3022/simple-chat-api-python/django:0.1").
		WithDirectory("./", client.Host().Directory("./apps"), dagger.ContainerWithDirectoryOpts{Owner: "django"}).
		WithServiceBinding("db", mysql).
		WithEnvVariable("DB_PASSWORD", mysqlPassword).
		WithEnvVariable("DB_HOST", "db").
		WithEnvVariable("DB_USERNAME", "root").
		WithEnvVariable("DB_NAME", "db_dev").
		WithEnvVariable("DB_PORT", "3306").
		WithExec([]string{"pip", "install", "-U", "-r", "requirements.txt"}).
		WithExec([]string{"cp", "sample.env", ".env"}).
		WithExec([]string{"pytest"})

	_, err = django.Stdout(ctx)
	if err != nil {
		fmt.Println(err)
	}
}
