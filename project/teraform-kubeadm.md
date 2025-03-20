# Create cube project with tree master and tree worker machines using Terraform yandex cloud and kubeadm.
## Infrastructure
  - Pre setup scenario
  Install Terraform according to installation guide.
  - [yandex cloud terrafform](https://yandex.cloud/en/docs/tutorials/infrastructure-management/terraform-quickstart#install-terrafor)
  Create a project / configuration [Teraform Best Practice ](https://www.terraform-best-practices.com/code-structure#getting-started-with-the-structuring-of-terraform-configurations) conform. 
  Install Yandex-cloud interface 

  ``` shell 
    curl -sSL https://storage.yandexcloud.net/yandexcloud-yc/install.sh | bash
```

Add role  to existing account
```shell
yc resource-manager folder  add-access-binding default --role editor --subject serviceAccount:aje231fn1irq80v3mj2c
```

Create service account key 
Создайте авторизованный ключ для сервисного аккаунта и запишите его файл:

``` shell
yc iam key create --service-account-id aje231fn1irq80v3mj2c --folder-name default --output key.json
```
