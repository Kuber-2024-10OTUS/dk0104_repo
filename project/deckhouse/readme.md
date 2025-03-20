# Terraform Deckhouse installation 
## Create user named deckhous 

``` shell
dk0104_repo/project/cloud-terraform on  exam-project [✘!?] via 💠 default took 12s
❯ yc iam service-account create --name deckhouse
done (2s)
id: aje2m1di05lksdu56vs0
folder_id: b1gekkfqv8u5qbjmnk5n
created_at: "2025-03-08T18:50:38.904686264Z"
name: deckhouse
```

## Assign the editor role to the newly created user:

```shell
yc resource-manager folder add-access-binding <folderID> --role editor --subject serviceAccount:<userID>

```
