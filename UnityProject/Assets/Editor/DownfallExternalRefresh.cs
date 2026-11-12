using System;
using System.IO;
using UnityEditor;
using UnityEngine;

// Allows a local, explicit refresh request without taking focus from another app.
[InitializeOnLoad]
internal static class DownfallExternalRefresh
{
    private static readonly string RequestPath = Path.GetFullPath(Path.Combine(Application.dataPath, "..", "Temp", "DownfallExternalRefresh.request"));
    private static double nextCheck;

    static DownfallExternalRefresh()
    {
        EditorApplication.update += CheckForRequest;
    }

    private static void CheckForRequest()
    {
        if (EditorApplication.timeSinceStartup < nextCheck)
            return;
        nextCheck = EditorApplication.timeSinceStartup + 1.0;

        if (EditorApplication.isPlayingOrWillChangePlaymode || EditorApplication.isCompiling || EditorApplication.isUpdating)
            return;

        try
        {
            if (!File.Exists(RequestPath))
                return;
            File.Delete(RequestPath);
            Debug.Log("DOWNFALL_EXTERNAL_REFRESH: request received");
            AssetDatabase.Refresh();
        }
        catch (IOException exception)
        {
            Debug.LogError("DOWNFALL_EXTERNAL_REFRESH: " + exception.Message);
        }
        catch (UnauthorizedAccessException exception)
        {
            Debug.LogError("DOWNFALL_EXTERNAL_REFRESH: " + exception.Message);
        }
    }
}
