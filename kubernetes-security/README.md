# Выполнено ДЗ №4 по теме "Настройка сервисных аккаунтов и ограничение прав для них"

- [x] Основное ДЗ

- [x] Задание со \*

## В процессе сделано:

В namespace homework создать service account monitoring
и дать ему доступ к эндпоинту /metrics вашего кластера

- Monitoring service account created which grant the access to /metrics endpoint using cluster role and according role binding
- Service Account and according Cluster role and Binding
  [monitoring-roles-binding](monitoring-roles-binging.yaml)
- Deployment with the Service account specification
  [deployment](deployment.yaml)

  ```yaml
  ....
  22 automountServiceAccountToken: true
  ....
  53 serviceAccountName: monitoring
  ....

  ```

- Cluster role admin -> cd service account binding
  [cd serviceAccount with according admin role binding](cd-roles-bindig.yaml)
  [permanent cd account configuration token ](cd-config-secret.yaml)

## Как запустить проект:

```
 kubectl apply -k .
```

## Как проверить работоспособность:

## PR checklist:

- [x] Выставлен label с темой домашнего задания
