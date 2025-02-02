{{- define "hwChart.name" -}}
{{ printf "%s-%s" .Chart.Name .Values.fullName  | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "hwChart.default.name" -}}
{{ default .default .name  }}
{{- end }}


{{- define "hwChart.configmap.name" -}}
{{ printf "%s-%s-configmap" (include "hwChart.name" .Values.configmap ) .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "hwChart.storageclass.name" -}}
{{ printf "%s-%s" (include "hwChart.name" .Values.storageClass ) .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- define "hwChart.pvc.name" -}}
{{ printf "%s-%s" (include "hwChart.name" .Values.persistentVolumeClaim ) .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "hwChart.labels" -}}
app: {{ include "hwChart.name" . }}
{{- end }}
